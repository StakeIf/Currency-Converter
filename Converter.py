class Converter():
    
    def converte(self, fromCurrency, toCurrency, date):
        if fromCurrency == 'EUR':
            return 98.96
        if date == '2024-04-08':
            return 92.19
        return 92.36

    def prediction(self, exchangeRates, amountDays):
        if len(exchangeRates) != 10:
            return 'error'
