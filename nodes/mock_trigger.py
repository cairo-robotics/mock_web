#!/usr/bin/env python

import rospy
from mock_web.mock_classes import MockTrigger
from std_msgs.msg import Bool


if __name__ == '__main__':
    rospy.init_node('mock_web_test')
    mock_trigger_1 = MockTrigger("Trigger 1")
    mock_trigger_2 = MockTrigger("Trigger 2")

    sub1 = rospy.Subscriber('/mock_trigger_1', Bool, mock_trigger_1.callback)
    sub2 = rospy.Subscriber('/mock_trigger_2', Bool, mock_trigger_2.callback)
    rospy.spin()    