#!/usr/bin/env python

import rospy, mopiapi
from mopi_msgs.srv import *
from mopi_msgs.msg import *
from std_msgs.msg import Float32

__mymopi = mopiapi.mopiapi()

def info_callback(req):
	ret = mopi_info()

	vv = __mymopi.getFirmwareVersion()
	ret.mayor_ver = vv[0]
	ret.minor_ver = vv[1]

	s = mopiapi.status(__mymopi.getStatus())		

	ret.status.active = s.SourceOneActive()

	ret.status.profile = 'User defined profile'	
	if not s.UserConfiguration():
		if s.JumperState():
			ret.status.profile = 'NiMH battery profile'
		else:			
			ret.status.profile = 'Alkaline battery profile'
	
	ret.status.good = s.CheckSourceOne()

	cnf = __mymopi.readConfig(1)

	if cnf[0] == 1:
		ret.cnf.src_type = "Rechargeable batteries"
	elif cnf[0] == 2:
		ret.cnf.src_type = "Non-rechargeable batteries"
	elif cnf[0] == 3:
		ret.cnf.src_type = "PSU / DC adapter"

	ret.cnf.lvls.maximum = cnf[1]
	ret.cnf.lvls.good = cnf[2]
	ret.cnf.lvls.low = cnf[3]
	ret.cnf.lvls.critical = cnf[4]

	return ret


def start_server():
	rospy.init_node("mopi_info_server")
	s = rospy.Service("mopi_info", MopiInfo, info_callback)
	print("Avvio il servizio...")
	rospy.spin()


if __name__ == "__main__":
	start_server()
