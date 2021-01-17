'''
 Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
  количества слов в каждой строке.
'''
#Вариант 1.Количество слов не считает.


my_list = ['New York is a capital of USA\n', 'Москва столица России\n', 'London is a capital of GB\n']
with open('text2.txt', 'w+', encoding='utf-8') as f:
    f.writelines(my_list)

with open('text2.txt', encoding='utf-8') as f:
    lines = 0
    letters =0
    for line in f:
        lines += line.count('\n')
        letters = len(line) - 1
        print(f"{letters} - количество символов в строке")
    print(f"Количество строк:  {lines}")


#Вариант 2.  В этом случае результат переписывает исходный  файл, но считает строки и слова предыдущего.

with open('text2.txt') as f:
    lines = f.readlines()
with open('text2.txt', 'w', encoding='utf-8') as f:
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        f.write('Line number {} has {} words.\n'.format(index + 1, number_of_words))
    #print('Line number {} has {} words.\n'.format(index + 1, number_of_words))
with open('text2.txt') as f:
    print(f.read())


