#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *

def robotDriver_client(speed, steer, command):
    rospy.wait_for_service('robotDriver')
    try:
        server = rospy.ServiceProxy('robotDriver', RobotDriver)
        resp1 = server(speed, steer, command)
        return resp1.status
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [speed steer command]"%sys.argv[0]

if __name__ == "__main__":
    """
    if len(sys.argv) == 4:
        speed = int(sys.argv[1])
        steer = int(sys.argv[2])
        command = int(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    """
    speed=100
    steer=100
    command='FORWARD'
    print "Requesting %s,%s,%s"%(speed, steer, command)
    print "%s"%(robotDriver_client(speed, steer, command))