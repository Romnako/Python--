'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''

name = input('enter name')
surname = input('enter surname')
year = int(input('enter year'))
city = input('enter city')
email = input('enter email')
telephone = input('input telephone')

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(f'Имя: {name}, Фамилия: {surname}, Возраст: {year},Город: {city} ,Почта: {email}, Телефон: {telephone}')

print(f"\nДругой вариант\n{'*' * 50}")


def my_fun(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])

print(my_fun(surname='Pop', name='Roma', year='45', city='Arkhangelsk', email='romnako.ru',
              telephone='00003'))

