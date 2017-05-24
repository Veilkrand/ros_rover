#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from ros_rover.msg import Rover
from SimpleUDPServer import SimpleUDPServer
from numpy import interp

server=SimpleUDPServer("",5005)

def talker():
    #pub = rospy.Publisher('chatter', String, queue_size=0)
    pub = rospy.Publisher('chatter', Rover, queue_size=0)
    rospy.init_node('talker', anonymous=True)
    # rate = rospy.Rate(1000) # 10hz
    while not rospy.is_shutdown():
        data=server.listen(False) #True for verbose
        
        steer=int(interp(data['axis'][2],[-1,1],[-255,255]))
        speed=int(interp(data['axis'][4],[-1,1],[0,255]))
        back_speed=int(interp(data['axis'][5],[-1,1],[0,255]))

        camera_pan_axis=0
        camera_tilt_axis=0
        camera_pan_button=0
        camera_tilt_button=0

        command='test'

        #rospy.loginfo(data)
        pub.publish(steer,speed,back_speed,camera_pan_axis,camera_tilt_axis,camera_pan_button,camera_tilt_button,command)
        #rate.sleep()
        #rospy.spin

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
