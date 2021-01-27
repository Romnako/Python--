'''
 Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
 методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
 и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Sum of complex numbers z1, z2 : ')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Product of complex numbers z1, z2 :')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + (self.a * other.b)} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
# Проверка результата
z_3 = (1 - 2j)
z_4 = (3 + 4j)
print(z_3)
print(z_4)
print(z_3 + z_4)
print(z_3 * z_4)
