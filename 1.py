
# Задача 1. 
print("Вас приветствует конвертер валют!")
usd = int(input("Введите курс USD сегодня: "))
eur = int(input("Введите курс EUR сегодня: "))
rub = int(input("Введите сумму RUB к обмену: "))
a = (usd)
b = (eur)
c = (rub)
d = round((c / a), 2)
print("Сумма к получению USD:", d)
d = round((c / b), 2)
print("Сумма к получению EUR:", d)
d = b / a
print("Коэффициент EUR/USD:", d)
print("Благодарим за обращение!")

