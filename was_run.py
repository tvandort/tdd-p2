from test_case import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun= None
        self.log = "setUp "

    def testMethod(self):
        self.wasRun= True
        self.log= self.log + "testMethod "

    def tearDown(self):
        self.log= self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception
