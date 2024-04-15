print('1. Узнать курс на сегодня')
print('2. Предсказать курс')

action = int(input('Выберите действие: '))
while action < 1 or action >2:
    action = int(input('Выберите действие: '))


if action == 1:
    print('\nВведите данные для конвертации (х Валюта1 --> Валюта2)')
    print('Где х - сколько валюты')
    print('Валюта1 - какую валюту конвертировать')
    print('Валюта2 - в какую валюту конвертировать')
    print('Список доступных валют: RUB, USD, EUR')

    x = input('\nx: ')
    fromCurrency =  input('Валюта1: ')
    toCurrency = input('Валюта2: ')
else:
    print('\nСписок доступных валют: RUB, USD, EUR')

    fromCurrency =  input('\nДля какой валюты предсказать курс: ')
    toCurrency =  input('Предсказать курс относительно какой валюты: ')
    amoutDays = input('На сколько дней вперед предсказать (до 10): ')


