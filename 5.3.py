'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''
staff = {'Соколов': 12000, 'Фролов': 17000, 'Васильев': 18400, 'Иванов': 19800, 'Чубайс': 5000000}
try:
    f = open('text3.txt', 'w', encoding='utf-8')
    for last_name, salary in staff.items():
        f.write(last_name + ':' + str(salary) + '\n')
except IOError:
    print('Произошла ошибка!')
finally:
    f.close()
summa = 0
score = 0
poor = []
with open('text3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
        persons = line.split(':')
        if int(persons[1]) < 20000:
            poor.append(persons[0])
        summa += int(persons[1])
        score += 1
result = summa / score
print(f'Низкооплачиваемые сотрудники : {poor}')
print(f'Средняя зарплата : {result}')
print('В среднем - все миллионеры ', ':)')











