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

    def test_converte_EURtoRUB20240401_9896(self):
        converter = Converter()
        fromCurrency = 'EUR'
        toCurrency = 'RUB'
        date = '2024-04-01'

        result = converter.converte(fromCurrency, toCurrency, date)
        
        expected = 98.96
        self.assertEqual(result, expected)

    
    def test_prediction_fewExchangeRates_error(self):
        converter = Converter()
        exchangeRates = [81, 82, 83]
        amountDays = 5

        result = converter.prediction(exchangeRates, amountDays)
        
        expected = 'error'
        self.assertEqual(result, expected)

    def test_prediction_lotExchangeRates_error(self):
        converter = Converter()
        exchangeRates = [81, 82, 83, 80, 90, 57, 90, 10, 90, 87, 66]
        amountDays = 5

        result = converter.prediction(exchangeRates, amountDays)
        
        expected = 'error'
        self.assertEqual(result, expected)

    def test_prediction_1(self):
        converter = Converter()
        exchangeRates = [92.2, 92.01, 91.78, 91.73, 91.84, 92.57, 92.57, 92.19, 92.00, 92.06]
        amountDays = 3

        result = converter.prediction(exchangeRates, amountDays)
        
        expected = [92.23, 92.25, 92.28]
        self.assertEqual(result, expected)

    def test_prediction_2(self):
        converter = Converter()
        exchangeRates = [92, 87, 90, 91, 91, 93, 92, 89, 90, 88]
        amountDays = 5

        result = converter.prediction(exchangeRates, amountDays)
        
        expected = [87.37, 86.4, 85.43, 84.46, 83.5]
        self.assertEqual(result, expected)
    
    def test_calculate_92mul3_276(self):
        converter = Converter()
        rate = 92
        value = 3

        result = converter.calculate(rate, value)
        
        expected = 276
        self.assertEqual(result, expected)

    def test_calculate_18mul05_9(self):
        converter = Converter()
        rate = 18
        value = 0.5

        result = converter.calculate(rate, value)
        
        expected = 9
        self.assertEqual(result, expected)

    def test_calculate_negative_error(self):
        converter = Converter()
        rate = -18
        value = -0.5

        result = converter.calculate(rate, value)
        
        expected = 'error'
        self.assertEqual(result, expected)

    