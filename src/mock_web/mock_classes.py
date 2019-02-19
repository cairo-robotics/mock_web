import rospy


class MockTrigger():

    def __init__(self, name):
        self.name = name
        self.triggered = False

    def callback(self, data):
        if data.data is True:
            self.triggered = True
            print "{} triggered!".format(self.name)


class MockToggle():

    def __init__(self, name):
        self.name = name
        self.toggled = False

    def callback(self, data):
        if data.data is True:
            self.toggled = True
            print "{} toggled!".format(self.name)