from test_result import TestResult

class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        self.wasRun= None
        self.wasSetUp= True

    def tearDown(self):
        pass

    def run(self):
        result= TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result
