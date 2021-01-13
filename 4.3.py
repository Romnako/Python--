'''
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
'''

number = range(20, 241)
#print(number)
new_number = [el for el in number if el % 20 == 0 or el % 21 ==0]
print(new_number)



