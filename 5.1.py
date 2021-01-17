'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_list = []
while True:
    line = input('Введите текст \n')
    if line == '':
        print(my_list)
        exit()
    else:
        newLine = line + '\n'
        my_list.append(newLine)

    with open('text1.txt', 'w', encoding='utf-8') as f:
        f.writelines(my_list)













