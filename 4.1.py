'''
Реализовать скрипт с функцией расчета заработной платы. В расчете необходимо использовать формулу: (выработка в часах *
ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

from sys import argv
script_name, work_hour, bet, profit = argv

try:
    payment = int(work_hour) * int(bet) + int(profit)
    print(f'Ваша зарплата равна: {payment}')
except ValueError:
    print('Это не число')

'''Вариант функции
def payment():
    try:
        work_hour = float(input('Выработка в часах:'))
        bet = int(input('Ставка в час в денежном выражении:'))
        profit = int(input('Премия:'))
        payment = work_hour * bet + profit
        print(f'Заработная плата: {payment}')
    except ValueError:
        return print('Это не число')
payment()
'''