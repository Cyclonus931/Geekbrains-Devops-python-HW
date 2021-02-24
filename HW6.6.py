# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),Pencil (карандаш),Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title: str
    _message = "Start rendering"

    def draw(self):
        print(self._message)


class Pen(Stationery):
    title = 'Pen'
    _message = f"{title} is drawing on the paper"


class Pencil(Stationery):
    title = 'Pencil'
    _message = f"{title} is drawing in the album"


class Handle(Stationery):
    title = 'Handle '
    _message = f"{title} is drawing on the wall"


pen, pencil, handle = Pen(), Pencil(), Handle()
pen.draw()
pencil.draw()
handle.draw()
