#!/usr/bin/env python

import rospy
from mopi.srv import *
from mopi.msg import *
from std_msgs.msg import Float32

def info_callback(req):
	ret = mopi_info()

	ret.mayor_ver = 5
	ret.minor_ver = 2

	ret.status.active = True

	ret.status.profile = 'Alkaline battery profile'
	
	ret.status.good = True

	ret.cnf.src_type = "Rechargeable batteries"

	ret.cnf.lvls.maximum = 13
	ret.cnf.lvls.good = 12
	ret.cnf.lvls.low = 11
	ret.cnf.lvls.critical = 10

	return ret


def start_server():
	rospy.init_node("mopi_info_server")
	s = rospy.Service("mopi_info", MopiInfo, info_callback)
	print("Avvio il servizio...")
	rospy.spin()


if __name__ == "__main__":
	start_server()
