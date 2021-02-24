# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.w
import time
from itertools import cycle


class TrafficLight:
    __color: str
    __counter: dict

    def __init__(self, red_count: int, yellow_count: int, green_count: int):
        self.__counter = {
            "red  - stop!": red_count,
            "yellow  - wait!": yellow_count,
            "green  - go!!!": green_count
        }

    def start(self):
        for color, mode in cycle(self.__counter.items()):
            self.__color = color

            for second in range(mode):
                print(f"{self} [{second + 1}]")
                time.sleep(1)

    def __repr__(self):
        return f"It's {self.__color}"


try:
    traffic_light = TrafficLight(7, 2, 7)
    traffic_light.start()
except TypeError:
    print("Wrong parameter")
except NameError:
    print("Wrong parameter")
