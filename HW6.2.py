# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    __length = float
    __width = float
    __mass = 12

    def __init__(self, length: float, width: float):
        self.__length = length
        self.__width = width

    def calculation(self, thickness: float = 1):
        return (self.__length * self.__width * self.__mass * thickness) / 1000


road = Road(20, 5000)
print(f'Overall mass needed : {road.calculation(40)}t')
