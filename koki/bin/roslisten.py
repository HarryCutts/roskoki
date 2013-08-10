#!/usr/bin/env python

# A basic drone controller class for the tutorial "Up and flying with the AR.Drone and ROS | Getting Started"
# https://github.com/mikehamer/ardrone_tutorials_getting_started

# This class implements basic control functionality which we will be using in future tutorials.
# It can command takeoff/landing/emergency as well as drone movement
# It also tracks the drone state based on navdata feedback

# Import the ROS libraries, and load the manifest file which through <depend package=... /> will give us access to the project dependencies
import roslib; roslib.load_manifest('koki')
import rospy

# Import the messages we're interested in sending and receiving
from geometry_msgs.msg import Twist  	 # for sending commands to the drone
from std_msgs.msg import Empty       	 # for land/takeoff/emergency
from ardrone_autonomy.msg import Navdata # for receiving navdata feedback

# An enumeration of Drone Statuses
from drone_status import DroneStatus

# Import custom message data.
from koki.msg import KokiMsg

#Import drone controller
'''from koki.bin.drone_controller import BasicDroneController'''


# Some Constants
COMMAND_PERIOD = 100 #ms



#Drone Controller

class BasicDroneController(object):
	def __init__(self):
		# Holds the current drone status
		self.status = -1

		# Subscribe to the /ardrone/navdata topic, of message type navdata, and call self.ReceiveNavdata when a message is received
		self.subNavdata = rospy.Subscriber('/ardrone/navdata',Navdata,self.ReceiveNavdata) 
		
		# Allow the controller to publish to the /ardrone/takeoff, land and reset topics
		self.pubLand    = rospy.Publisher('/ardrone/land',Empty)
		self.pubTakeoff = rospy.Publisher('/ardrone/takeoff',Empty)
		self.pubReset   = rospy.Publisher('/ardrone/reset',Empty)
		
		# Allow the controller to publish to the /cmd_vel topic and thus control the drone
		self.pubCommand = rospy.Publisher('/cmd_vel',Twist)

		# Setup regular publishing of control packets
		self.command = Twist()
		self.commandTimer = rospy.Timer(rospy.Duration(COMMAND_PERIOD/1000.0),self.SendCommand)

		# Land the drone if we are shutting down
		rospy.on_shutdown(self.SendLand)

	def ReceiveNavdata(self,navdata):
		# Although there is a lot of data in this packet, we're only interested in the state at the moment	
		self.status = navdata.state

	def SendTakeoff(self):
		# Send a takeoff message to the ardrone driver
		# Note we only send a takeoff message if the drone is landed - an unexpected takeoff is not good!
		if(self.status == DroneStatus.Landed):
			self.pubTakeoff.publish(Empty())

	def SendLand(self):
		# Send a landing message to the ardrone driver
		# Note we send this in all states, landing can do no harm
		self.pubLand.publish(Empty())

	def SendEmergency(self):
		# Send an emergency (or reset) message to the ardrone driver
		self.pubReset.publish(Empty())

	def SetCommand(self,roll=0,pitch=0,yaw_velocity=0,z_velocity=0):
		# Called by the main program to set the current command
		self.command.linear.x  = pitch
		self.command.linear.y  = roll
		self.command.linear.z  = z_velocity
		self.command.angular.z = yaw_velocity

	def SendCommand(self,event):
		# The previously set command is then sent out periodically if the drone is flying
		if self.status == DroneStatus.Flying or self.status == DroneStatus.GotoHover or self.status == DroneStatus.Hovering:
			self.pubCommand.publish(self.command)



##############





# Initialize the node and name it.
rospy.init_node('kokilisten', anonymous = True)

#Initialize drone controller
droneController = BasicDroneController()

# Create a callback function for the subscriber.
def callback(data):
    # Simply print out values in our custom message.
    rospy.logwarn(rospy.get_name() + " I heard %s", data.tags)
    tags = list(data.tags)
    if 162 in tags: droneController.SendTakeoff() #yellow
    elif 141 in tags: droneController.SendLand() #green
    elif 158 in tags: #pink
	    droneController.SetCommand(yaw_velocity=10.)
	    droneController.SendCommand(None)
    else:
	    droneController.SetCommand(yaw_velocity=0.)
	    droneController.SendCommand(None)


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

    droneController.SendTakeoff()

    # Go to the main loop.
    listener()
