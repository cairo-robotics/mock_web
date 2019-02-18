#!/usr/bin/env python

import rospy
from mock_web.mock_classes import MockTrigger
from std_msgs.msg import Bool


if __name__ == '__main__':
    mock_trigger = MockTrigger()
    rospy.init_node('mock_web_test')

    sub = rospy.Subscriber('mock_trigger', Bool, mock_trigger.callback)
    rospy.spin()    