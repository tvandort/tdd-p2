from test_case import TestCase

class BrokenSetup(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        raise Exception

    def testMethod(self):
        pass
