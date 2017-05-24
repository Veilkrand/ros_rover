##
TODO:
- Show latency from UDP timestamp
- Change names to a real project:
-- `beginner_tutorials`
-- `listener.py`, `talker.py`, chatter topic
- Being able to control over 3G

## Start Working environment
cd ~/ros_catkin_ws
. ~/ros_catkin_ws/devel/setup.bash
roscd ros_rover

## Build package
> Only first time when you have a new one.
~/ros_catkin_ws
catkin_make

## Start Core
nohup roscore &
## Stop Core
killall -9 roscore
killall -9 rosmaster
--
# Nodes

talker.py (UDP Server) -> ['chatter' topic] <- lister.py (robot Controller)

## Start nodes

nohup rosrun ros_rover talker.py &
rosrun ros_rover listener.py

## Kill Node
ps aux | grep scripts/talker.py
kill -9 pid

## Echo topic node
rostopic echo chatter

## list topics
rostopic list

---
# New Node
1. Create a new python inside src/[package_name]/scripts
2. Make executable `chmod +x [myscript].py`
.....

Create MSG and SRV
http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv#Creating_a_srv
##

---
# Create a new ROS package
cd ~/ros_catkin_ws/src
catkin_create_pkg ros_rover std_msgs rospy roscpp
catkin_make
. ~/ros_catkin_ws/devel/setup.bash
rospack depends1 ros_rover
