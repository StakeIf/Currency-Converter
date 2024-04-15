from Converter import Converter

converter = Converter()

print('1. Узнать курс на сегодня')
print('2. Предсказать курс')
print('3. История курса')

action = int(input('Выберите действие: '))
while action < 1 or action >3:
    action = int(input('Выберите действие: '))

if action == 1:
    print('\nВведите данные для конвертации (х Валюта1 --> Валюта2)')
    print('Где х - сколько валюты')
    print('Валюта1 - какую валюту конвертировать')
    print('Валюта2 - в какую валюту конвертировать')
    print('Список доступных валют: RUB, USD, EUR')

    value = input('\nx: ')
    fromCurrency =  input('Валюта1: ')
    toCurrency = input('Валюта2: ')

    print('Текущий курс: ', converter.actionConverte(int(value), fromCurrency, toCurrency))

elif action == 2:
    print('\nСписок доступных валют: RUB, USD, EUR')

    fromCurrency =  input('\nДля какой валюты предсказать курс: ')
    toCurrency =  input('Предсказать курс относительно какой валюты: ')
    amountDays = input('На сколько дней вперед предсказать (до 10): ')

    converter.actionPrediction(fromCurrency, toCurrency, int(amountDays))

else:
    print('\nСписок доступных валют: RUB, USD, EUR')

    fromCurrency =  input('\nДля какой валюты вывести историю: ')
    toCurrency =  input('История относительно какой валюты: ')
    amountDays = input('На сколько дней назад вывести историю (до 10): ')

    converter.actionHistory(fromCurrency, toCurrency, int(amountDays))