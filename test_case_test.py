from test_case import TestCase
from test_result import TestResult
from was_run import WasRun
from broken_setup import BrokenSetup
from test_suite import TestSuite


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test= WasRun("testMethod")
        result= TestResult()
        test.run(result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test= WasRun("testMethod")
        result= TestResult()
        test.run(result)
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test= WasRun("testBrokenMethod")
        result= TestResult()
        test.run(result)
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result= TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def setupFailed(self):
        test= BrokenSetup("testMethod")
        result= TestResult()
        test.run(result)
        assert("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite= TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result= TestResult()
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())

# tests = [f for _, f in TestCaseTest.__dict__.items() if callable(f)]

# for test in tests:
#     result= TestResult()
#     TestCaseTest(test.__name__).run(result)
#     print(test.__name__)
#     print(result.summary())

suite= TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("setupFailed"))
result= TestResult()
suite.run(result)
print(result.summary())

