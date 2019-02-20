#!/bin/bash
source /opt/ros/kinetic/setup.bash
source /home/ros_ws/devel/setup.sh
roslaunch mock_web mock_server.launch
rqt