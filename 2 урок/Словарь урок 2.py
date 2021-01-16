data = []
menu = '1. Ввести данные\n2. Вывести данные\n3. Выход'
while True:

    print(menu)
    change = input('Выберите пункт меню: ')

    if change == '1':
        person = input('Введите имя и возраст через пробел: ').split()
        user_db = {
            'name': person[0],
            'age': person[1]
        }
        data.append(user_db)

    elif change == '2':
        print(data)

    elif change == '3':
        break

    else:
        print('Повторите ввод!')
