from test_case import TestCase
from test_result import TestResult
from was_run import WasRun
from broken_setup import BrokenSetup
from test_suite import TestSuite


class TestCaseTest(TestCase):
    def setUp(self):
        self.result= TestResult()

    def testTemplateMethod(self):
        test= WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test= WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test= WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def setupFailed(self):
        test= BrokenSetup("testMethod")
        try:
            test.run(self.result)
            assert False
        except:
            pass

    def testSuiteContainsFailingSetup(self):
        suite= TestSuite()
        suite.add(BrokenSetup("testMethod"))
        suite.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite= TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

    def tearDownIfFailed(self):
        test= WasRun("testBrokenMethod")
        test.run(self.result)

suite= TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("setupFailed"))
suite.add(TestCaseTest("testSuiteContainsFailingSetup"))
suite.add(TestCaseTest("tearDownIfFailed"))

result= TestResult()
suite.run(result)
print(result.summary())

