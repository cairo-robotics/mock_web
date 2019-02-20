#!/bin/bash
cd /home/ros_ws/
rm -r build/ devel/
source /opt/ros/kinetic/setup.bash
catkin_make
source devel/setup.sh
