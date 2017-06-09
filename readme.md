## Nodes
A[talker.py] -- Create Service --> B(chatter)
C[listener.py] == Subscribe ==> B(chatter)
D[pantilt_listener.py] == Subscribe ==> B(chatter)


---
## TODO:
- Show latency from UDP timestamp
	- Timestamp in messsages
	- Calculate latency in SimpleServer
- Rename `listener.py`, `talker.py`, chatter topic
- Being able to control over 3G
- Main dashboard
- Control Lights

---
# PS4 Controls:

## Camera Control:
- Pad: Move camera center
- R Axis: Look camera around
- R3 Button: Center Camer
## Movement control
- L Axis: Steering
- R2: Accelerate forward
- L2: Accelerate backwards

---
# Work Setup

## Start controller client in local machine
python client.py -h 10.8.0.10 --python2

## Mount FS
sudo sshfs -o allow_other,defer_permissions pi@10.8.0.10:/ /Users/alberto.naranjo/Documents/Raspberry\ PI/mount

## Start working and launch from home/
. start_ros.bash


---

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
