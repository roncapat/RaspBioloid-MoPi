#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

def publisher():
	print("Avvio il publisher...")
	pub = rospy.Publisher('battery_lvl', Float32, queue_size=5)
	rospy.init_node("publisher", anonymous=True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		pub.publish(12.4)
		rate.sleep()

if __name__ == "__main__":
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass
