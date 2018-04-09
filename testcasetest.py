from testcase import TestCase
from wasrun import WasRun

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

TestCaseTest("testTemplateMethod").run()