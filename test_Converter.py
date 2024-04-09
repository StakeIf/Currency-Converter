import unittest

class ListHandlerTests(unittest.TestCase):

    def test_ClassCreation(self):
        converter = Converter()
        self.assertIsNotNone(converter)