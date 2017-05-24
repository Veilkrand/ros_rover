#!/usr/bin/env python
from beginner_tutorials.srv import *
import rospy

def handle_drive(req):
  print "Speed %s"%(req.speed) ,
  return str(req.speed)

def add_server():
  rospy.init_node('robotDriver_server')
  s = rospy.Service('robotDriver', RobotDriver, handle_drive)
  print "Ready."
  rospy.spin()

if __name__ == "__main__":
  add_server()