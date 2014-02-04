#!/usr/bin/env python

# Import required Python code.
import roslib
roslib.load_manifest('koki')
import rospy

# Import custom message data.
from koki.msg import KokiMsg

# Create a callback function for the subscriber.
def callback(data):
    # Simply print out values in our custom message.
    rospy.logwarn(rospy.get_name() + " I heard %s", data.tags)

# This ends up being the main while loop.
def listener():
    # Get the ~private namespace parameters from command line or launch file.
    topic = rospy.get_param('~topic', 'koki_tags')
    # Create a subscriber with appropriate topic, custom message and name of callback function.
    rospy.Subscriber(topic, KokiMsg, callback)
    # Wait for messages on topic, go to callback function when new messages arrive.
    rospy.spin()

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node('kokilisten', anonymous = True)

    # Go to the main loop.
    listener()
