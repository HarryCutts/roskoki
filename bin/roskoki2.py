#!/usr/bin/env python
from pykoki import PyKoki, Point2Di, Point2Df, CameraParams
import cv, cv2
import sys

import roslib
roslib.load_manifest('koki')
import sys
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from koki.msg import *

class roskoki:

    def __init__(self):
        self.tag_pub = rospy.Publisher("koki_tags",KokiMsg)
        self.marker_pub = rospy.Publisher("koki_markers",Kokimarkers)

        cv.NamedWindow("Image window", 1)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("image_topic",Image,self.callback)

        self.koki = PyKoki()


    def callback(self,data):
        try:
            cv_image = cv.GetImage(self.bridge.imgmsg_to_cv(data, "mono8")) 

            koki_params = CameraParams(Point2Df( cv_image.width/2, cv_image.height/2 ),
                                       Point2Df(571, 571),
                                       Point2Di( cv_image.width, cv_image.height ))

            markers = self.koki.find_markers( cv_image, 0.1, koki_params )

            seencodes=[]
            seenmarkers=[]
            for m in markers:
                markerinfo=Kokimarker()
                rospy.loginfo("Code: " + str(m.code))
                rospy.loginfo("Bearing: " + str(m.bearing))
                rospy.loginfo("distance: " + str(m.distance))
                seencodes.append(m.code)
                markerinfo.ID = m.code
                markerinfo.bearing = m.bearing
                markerinfo.distance = m.distance
                seenmarkers.append(markerinfo)
                    

        except CvBridgeError, e:
            rospy.logwarn(str(e))
            """print 'did not get image'"""

#        cv.ShowImage("Image window", cv_image)
#        cv.WaitKey(3)

        tags = KokiMsg()
        tags.tags = seencodes

        details = Kokimarkers()
        details.markers = seenmarkers

        try:
            self.tag_pub.publish(tags)
            self.marker_pub.publish(details)
        except CvBridgeError, e:
            print e

def main(args):
    rospy.init_node('koki_marker_finder', anonymous=True)
    ic = roskoki()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"

    cv.DestroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)

