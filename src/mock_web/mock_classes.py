class MockTrigger():

    def __init__(self):
        self.triggered = False

    def callback(self, data):
        if data.data is True:
            self.triggered = True
            print "Triggered!"
