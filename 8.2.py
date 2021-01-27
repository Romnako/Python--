'''
 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
 ситуацию и не завершиться с ошибкой.
'''


class Zero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_zero(divider, denominator):
        try:
            return (divider / denominator)

        except:
            print(f'Division by zero is not allowed!')


ddiv = Zero(10, 100)
print(ddiv)
print(Zero.divide_zero(10, 0))
print(Zero.divide_zero(10, 0.1))
print(ddiv.divide_zero(100, 0))
