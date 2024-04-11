import unittest
from Converter import Converter

class ConverterTests(unittest.TestCase):

    def test_ClassCreation(self):
        converter = Converter()
        self.assertIsNotNone(converter)

    def test_converte_USDtoRUB20240408_9219(self):
        converter = Converter()
        fromCurrency = 'USD'
        toCurrency = 'RUB'
        date = '2024-04-08'

        result = converter.converte(fromCurrency, toCurrency, date)
        
        expected = 92.19
        self.assertEqual(result, expected)

    def test_converte_USDtoRUB20240410_9236(self):
        converter = Converter()
        fromCurrency = 'USD'
        toCurrency = 'RUB'
        date = '2024-04-10'

        result = converter.converte(fromCurrency, toCurrency, date)
        
        expected = 92.36
        self.assertEqual(result, expected)