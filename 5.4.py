'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

rus_number = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text4.txt', 'w', encoding='utf-8') as file_1:
    file_1.writelines(rus_number)
    with open('text4.txt', 'r', encoding='utf-8') as file_1:
        for i in file_1:
            i = i.split(' ', 1)
            new_file.append(rus_number[i[0]] + ' ' + i[1])
print(new_file)
with open('text4_new.txt', 'w', encoding='utf-8') as file_2:
    file_2.writelines(new_file)
print(new_file)

