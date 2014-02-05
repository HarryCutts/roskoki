#!/usr/bin/env python
from pykoki import PyKoki, Point2Di, Point2Df, CameraParams
import cv, cv2
import sys

import roslib
roslib.load_manifest('koki')
import sys
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from koki.msg import *

def _koki_point_to_msg(point):
    return Point(x = point.x, y = point.y, z = point.z if hasattr(point, 'z') else 0)

def _koki_vertex_to_msg(struct):
    return MarkerVertex(image = _koki_point_to_msg(struct.image), world = _koki_point_to_msg(struct.world))

class roskoki:

    def __init__(self):
        self.code_pub = rospy.Publisher("koki_codes", KokiCodeArray)
        self.marker_pub = rospy.Publisher("koki_markers", KokiFrame)

        cv.NamedWindow("Image window", 1)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("image_topic",Image,self.callback)

        self.koki = PyKoki('/usr/lib')


    def callback(self,data):
        try:
            cv_image = cv.GetImage(self.bridge.imgmsg_to_cv(data, "mono8")) 

            koki_params = CameraParams(Point2Df( cv_image.width/2, cv_image.height/2 ),
                                       Point2Df(571, 571),
                                       Point2Di( cv_image.width, cv_image.height ))

            markers = self.koki.find_markers( cv_image, 0.155, koki_params )  # TODO: allow for different marker sizes

            seen_codes   = []
            seen_markers = []
            for m in markers:
                marker = KokiMarker(code            = m.code,
                                    center          = _koki_vertex_to_msg(m.centre),
                                    vertices        = (_koki_vertex_to_msg(vertex) for vertex in m.vertices),
                                    rotation_offset = m.rotation_offset,
                                    rotation        = _koki_point_to_msg(m.rotation),
                                    bearing         = _koki_point_to_msg(m.bearing),
                                    distance        = m.distance)
                seen_codes.append(m.code)
                seen_markers.append(marker)
                rospy.loginfo("Code: " + str(m.code))
                rospy.loginfo("Bearing: " + str(m.bearing))
                rospy.loginfo("distance: " + str(m.distance))
                    

        except CvBridgeError, e:
            rospy.logwarn(str(e))
            """print 'did not get image'"""

#        cv.ShowImage("Image window", cv_image)
#        cv.WaitKey(3)

        code_array = KokiCodeArray()
        code_array.codes = seen_codes

        frame = KokiFrame()
        frame.markers = seen_markers

        try:
            self.code_pub.publish(code_array)
            self.marker_pub.publish(frame)
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

