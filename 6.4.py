'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'{self.name}  over speed for town car'
        else:
            return f'{self.name}  normal speed for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'{self.name} over speed for work car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name}  from police '
        else:
            return f'{self.name}  not from police'


ferrari = SportCar(300, 'Red', 'Ferrari', False)
renault = TownCar(60, 'White', 'Renault', False)
lada = WorkCar(70, 'Brown', 'Lada', True)
ford = PoliceCar(110, 'White-Blue',  'Ford', True)
print(lada.turn_left())
print(f'When {renault.turn_left()}, then {ford.stop()}')
print(f'{lada.go()} with speed exactly {lada.show_speed()}')
print(f'{lada.name} is {lada.color}')
print(f'Is {ferrari.name} a police car? {ferrari.is_police}')
print(f'Is {lada.name}  a police car? {lada.is_police}')
print(ferrari.show_speed())
print(renault.show_speed())
print(ford.police())
print(ford.show_speed())
print(lada.show_speed())
print(ford.color)