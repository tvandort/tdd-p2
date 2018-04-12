from test_result import TestResult

class TestSuite:
    def __init__(self):
        self.tests= []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            try:
                test.run(result)
            except:
                result.testFailed()
        return result