# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:для пальто(V/6.5 + 0.5),для костюма(2*H+0.3)
# Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property
from abc import ABC, abstractmethod


class Clothes(ABC):
    clothes_type: str

    def __init__(self, clothes_type: str):
        self.clothes_type = clothes_type

    @abstractmethod
    def formula(self):
        pass


class Coat(Clothes):
    _size: float

    def __init__(self, clothes_type: str, size: float):
        super().__init__(clothes_type)
        self._size = size

    @property
    def formula(self):
        return self._size / 6.5 + 0.5


class Suit(Clothes):
    _height: float

    def __init__(self, clothes_type: str, height: float):
        super().__init__(clothes_type)
        self._height = height

    @property
    def formula(self):
        return 2 * self._height + 0.3


try:
    c = Coat("Coat", float(input("Enter a coat size >>> ")))
    s = Suit("Suit", float(input("Enter a height for the suit (in meters) >>> ")))
    print(f'For 1 {c.clothes_type} and 1 {s.clothes_type} you will need {round(c.formula + s.formula,2)} meters of cloth')
except ValueError:
    print("Wrong parameters")
