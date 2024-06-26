import datetime
import requests
from bs4 import BeautifulSoup

import numpy as np
from scipy.interpolate import UnivariateSpline

class Converter():
    def renameCurrency(self, currency):
        if currency == 'EUR':
            return 'Euro'
        if currency == 'USD':
            return 'US Dollar'
        return 'Russian Ruble'
    
    def converte(self, fromCurrency, toCurrency, date):
        # Адрес сайта, с которого мы будем получать данные
        url = "https://www.x-rates.com/historical/?from="+fromCurrency+"&date="+date
        
        # Получаем содержимое страницы
        response = requests.get(url)

        # Создаем объект BeautifulSoup для парсинга HTML-разметки
        soup = BeautifulSoup(response.content, "html.parser")

        exchange_tables = soup.find_all("table")
        exchange_rates = {}

        for exchange_table in exchange_tables:
            for tr in exchange_table.find_all("tr"):
                tds = tr.find_all("td")
                if tds:
                    currency = tds[0].text
                    exchange_rate = float(tds[1].text)
                    exchange_rates[currency] = exchange_rate        

        result = round(exchange_rates[self.renameCurrency(toCurrency)], 2)
        return result
    
    def prediction(self, exchangeRates, amountDays):
        if len(exchangeRates) != 10:
            return 'error'
        
        amountExchangeRates = len(exchangeRates)

        days = np.array([x for x in range(0, amountExchangeRates)])
        dayswanted = np.array([ x for x in range( 0, amountExchangeRates + amountDays)])

        extrapolator = UnivariateSpline( days, exchangeRates, k=1 )
        y = extrapolator( dayswanted )
        result = []

        for i in range(amountExchangeRates, amountExchangeRates+amountDays):
            result.append(round(y[i], 2))

        return result
    
    def calculate(self, rate, value):
        if (rate < 0 or value < 0):
            return 'error'
        return rate * value
    

    def actionConverte(self, value, fromCurrency, toCurrency):
        current_date = datetime.date.today().isoformat()
        rate = self.converte(fromCurrency, toCurrency, current_date)
        result = self.calculate(rate, value)
        return result


    def actionPrediction(self, fromCurrency, toCurrency, amountDays):
        datesAfterToday = []
        rates = []

        for i in range(9, -1, -1):
            day = (datetime.date.today() - datetime.timedelta(days=i)).isoformat()
            rates.append(self.converte(fromCurrency, toCurrency, day))

        for i in range(1, amountDays+1):
            day = (datetime.date.today() + datetime.timedelta(days=i)).isoformat()
            datesAfterToday.append(day)

        result = self.prediction(rates, amountDays)

        print("Текущий курс:", rates[9])

        for i in range(0, amountDays):
            print(datesAfterToday[i], ':', result[i])

    def actionHistory(self, fromCurrency, toCurrency, amountDays):
        datesBeforeToday = []
        rates = []

        for i in range(amountDays, 0, -1):
            day = (datetime.date.today() - datetime.timedelta(days=i)).isoformat()
            datesBeforeToday.append(day)
            rates.append(self.converte(fromCurrency, toCurrency, day))

        for i in range(0, amountDays):
            print(datesBeforeToday[i], ':', rates[i])