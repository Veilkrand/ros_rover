#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from ros_rover.msg import Rover
from Robot4WD import Robot4WD
from PanTilt import PanTilt

LEFT_TRIM   = 0
RIGHT_TRIM  = 0

robot = Robot4WD(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM,left_id1=1,right_id1=2,left_id2=3,right_id2=4)

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.speed)
    #print "\r%s"%data.speed,
    print "Forward: %s Backward:%s Steer:%s"%(data.forward_speed_axis,data.backward_speed_axis,data.steer_angle_axis)

    if (data.steer_angle_axis<0):
        robot.left(0, None)
        speed=abs(data.steer_angle_axis)
        robot._left_speed(speed)
        robot._right_speed(speed)
    elif (data.steer_angle_axis>0):
        robot.right(0, None)
        speed=abs(data.steer_angle_axis)
        robot._left_speed(speed)
        robot._right_speed(speed)
    elif (data.forward_speed_axis>0):
        robot.forward(0, None)
        robot._left_speed(data.forward_speed_axis)
        robot._right_speed(data.forward_speed_axis)
    elif (data.backward_speed_axis>0):
        robot.backward(0, None)
        robot._left_speed(data.backward_speed_axis)
        robot._right_speed(data.backward_speed_axis)
    else:
        robot.stop()

    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', Rover, callback,queue_size=1)

    rate = rospy.Rate(5)

    rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    #robot.forward(0, None)
    listener()
