'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Data:

    def __init__(self, data_month_year):
        self.data_month_year = str(data_month_year)

    @classmethod
    def extract(cls, data_month_year):
        my_day = []
        for i in data_month_year.split():
            if i != '-': my_day.append(i)
        return int(my_day[0]), int(my_day[1]), int(my_day[2])

    @staticmethod
    def valid(data, month, year):
        if 1 <= data <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 2020:
                    return f'Correct input '
                else:
                    return f'Incorrect year'
            else:
                return f'Incorrect month'
        else:
            return f'Incorrect day '

    def __str__(self):
        return f'Correct today data: {Data.extract(self.data_month_year)}'


data = Data('27_12_2021')
print(Data)
print(data.extract)
print(Data.valid(27, 1, 2021))

print(Data.valid(11, 12, 2022))
print(data.valid(11, 13, 2011))
print(Data.extract('2 - 11 - 2011'))
print(data.extract('11 - 11 - 2020'))
print(Data.valid(32, 12, 2020))
