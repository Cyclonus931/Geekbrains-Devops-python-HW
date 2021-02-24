# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed = int
    color = str
    name = str
    is_police = False

    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.color} {self.name}: start")

    def stop(self):
        print(f"{self.color} {self.name}: stop")

    def turn(self, direction: str):
        print(f"{self.color} {self.name}: turned {direction}")

    def show_speed(self):
        print(f"{self.color} {self.name}: speed = {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.color} {self.name}: Over speed!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.color} {self.name}"Over speed!"')


class PoliceCar(Car):
    is_police = True


sportcar = SportCar(200, "Purple", "Ferrari")
towncar = TownCar(61, "White", "Hyundai")
police = PoliceCar(180, "Blue & white", "Police car")
workcar = WorkCar(35,"Green","Isuzu")


sportcar.go()
sportcar.show_speed()
towncar.show_speed()
police.show_speed()
workcar.turn("left")
