class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        self.wasRun= None
        self.wasSetUp= True

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
