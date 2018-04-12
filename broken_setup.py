from was_run import WasRun

class BrokenSetup(WasRun):
    def __init__(self, name):
        WasRun.__init__(self, name)

    def setUp(self):
        self.testBrokenMethod()

    def testMethod(self):
        print('runs the method')

