'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''


class Cloth:
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    def get_square_coat(self):
        return self.size / 6.5 + 0.5

    def get_square_costume(self):
        return self.growth * 2 + 0.3

    @property
    def get_square_full(self):
        return str(f'Square of the cloth : \n'
                   f'{(self.size / 6.5 + 0.5) + (self.growth * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, size, growth):
        super().__init__(size, growth)
        self.get_square_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Square coat : {self.get_square_coat}'


class Costume(Cloth):
    def __init__(self, size, growth):
        super().__init__(size, growth)
        self.get_square_costume = round(self.growth * 2 + 0.3)

    def __str__(self):
        return f'Square costume : {self.get_square_costume}'


coat = Coat(2, 3)
costume = Costume(1, 4)
print(coat)
print(costume)
print(coat.get_square_full)
print(costume.get_square_coat)
print(costume.get_square_full)
print(coat.get_square_costume())
