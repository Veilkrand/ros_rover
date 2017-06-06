#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from ros_rover.msg import Rover
from numpy import interp
from PanTilt import PanTilt


pt = PanTilt()

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.speed)
    
    pan=int(interp(data.camera_pan_axis,[0,255],[-90,90]))
    tilt=int(interp(data.camera_tilt_axis,[0,255],[-90,90]))
    
    ## Switch!
    # pt.panTilt(pan,tilt)
    pt.panTilt(tilt,-pan)

    ## Switch!
    #pt.increaseOffset(data.camera_tilt_button,data.camera_pan_button)
    pt.increaseOffset(-data.camera_tilt_button,-data.camera_pan_button)

    print "(%s,%s) Pan: %s Tilt: %s "%(data.camera_pan_button,data.camera_tilt_button,pan,tilt)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('pantilt_listener', anonymous=True)

    rospy.Subscriber('chatter', Rover, callback,queue_size=1)

    rate = rospy.Rate(5)

    rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    
    listener()
