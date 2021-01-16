'''
Программа принимает действительное положительное число x
и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции
my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
'''
x = int(input('enter x :'))
y = int(input('enter y :'))

print(pow(x, y))

def x_pow(x, y):
    return x ** y
print(x_pow(x, y))

def my_func(x, y):
    return 1 / x ** abs(y)
print(my_func(x, y))

def my_fun(x, y):
    if x >= 0 and y < 0:
        return x ** y
print(my_fun(x, y))

