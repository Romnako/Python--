'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
def summ():
    try:
        with open('text5.txt', 'w+') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            my_number = line.split()

            print(sum(map(int, my_number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print(' Ошибка ввода')
summ()