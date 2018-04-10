from test_case import TestCase
from test_result import TestResult
from was_run import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test= WasRun("testMethod")
        result= test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test= WasRun("testBrokenMethod")
        result= test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result= TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

# TestCaseTest("testTemplateMethod").run()
# TestCaseTest("testResult").run()
# TestCaseTest("testFailedResult").run()

tests = [f for _, f in TestCaseTest.__dict__.items() if callable(f)]

for test in tests:
    TestCaseTest(test.__name__).run()
