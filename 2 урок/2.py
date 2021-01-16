
print('Генератор случайной строки')
gen = [c + d for c in 'cat' if c != 'i' for d in 'dog' if d != 'a'] #Генератор случайных
print(gen)
list.sort(gen)
print(gen)
print('-------------------->')
text = input('Введите список любых имен, слов и цифр через пробел').split()
print(text)
print('Новая последовательность')
list.sort(text)
print(text)

#"Это не получилось"

'''g = int(input('Введите список команд'))
g = [c * 2 for c in 'list' if c != 'i']
print(g)'''

'''n = int(input('Введите количество k элементов списка: '))
print('Введите содержимое каждого из k подсписков своими руками через пробел.')
A = [age]
for i in range(1, age+1):
    arr = list(input('Для перехода между подсписками k нажимайте Enter: ').split())
    arr[-1], arr[i] = arr[i], arr[-1]
    A.append(arr)
print(A)'''
'''print(list(age))
a = []
a = list(age)
print(a)
#name = split()
#print(name)'''

'''a = []  # заводим пустой список
n = int(input('Введите список любых имен и цифр через пробел'))  # считываем количество элемент в списке
print(n)
a = ()
for i in range(n):
    new_element = int(input())  # считываем очередной элемент
    a.append(new_element)  # добавляем его в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(a)'''