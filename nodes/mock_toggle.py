#!/usr/bin/env python

import rospy
from mock_web.mock_classes import MockToggle
from std_msgs.msg import Bool


if __name__ == '__main__':
    rospy.init_node('mock_web_test')
    mock_toggle_1 = MockToggle("Toggle 1")
    mock_toggle_2 = MockToggle("Toggle 2")

    sub1 = rospy.Subscriber('mock_toggle_1', Bool, mock_toggle_1.callback)
    sub2 = rospy.Subscriber('mock_toggle_2', Bool, mock_toggle_2.callback)
    pub1 = rospy.Publisher('mock_toggled_1', Bool, queue_size=10)
    pub2 = rospy.Publisher('mock_toggled_2', Bool, queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub1.publish(mock_toggle_1.toggled)
        pub2.publish(mock_toggle_2.toggled)
        rate.sleep()

    rospy.spin()