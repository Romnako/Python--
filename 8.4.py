'''
----4.
 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
 который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
 В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
 уникальные для каждого типа оргтехники.
----5.
 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
 определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
 других данных, можно использовать любую подходящую структуру, например словарь.
----6.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''


class Warehouse:
    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Device model': self.name, 'Unit price': self.price, 'Amount devices': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} amount devices {self.quantity}'

    def reception(self):

        try:
            unit = input(f'Input device model: ')
            unit_p = int(input(f'Input unit price: '))
            unit_q = int(input(f'Amount devices: '))
            unique = {'Device model': unit, 'Unit price': unit_p, 'Amount devices': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Сurrent list -\n {self.my_store}')
        except:
            return f'Data entry error'

        print(f'For exit - Q, Continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Whole warehouse -\n {self.my_store_full}')
            return f'Exit'
        else:
            return Warehouse.reception(self)


class OfficeEquipment(Warehouse):
    def off_equ(self):
        pass


class Printer(Warehouse):
    def to_print(self):
        return f'to print  {self.numb}'


class Scanner(Warehouse):
    def to_scan(self):
        return f'to scan  {self.numb}'


class Copier(Warehouse):
    def to_copier(self):
        return f'to copier   {self.numb}'


unit_1 = Printer('HP', 7500, 15, 10)
unit_2 = Scanner('Honor', 6200, 5, 10)
unit_3 = Copier('Xerox', 4500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
