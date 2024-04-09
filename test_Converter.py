import unittest
from Converter import Converter

class ListHandlerTests(unittest.TestCase):

    def test_ClassCreation(self):
        converter = Converter()
        self.assertIsNotNone(converter)