from test_case import TestCase

class BrokenSetup(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        pass
    def testMethod(self):
        pass
