# Реализовать базовый класс Worker (работник),в котором определить атрибуты: name, surname,position (должность),
# income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = str
    surname = str
    position = str
    __income = dict

    def __init__(self, name: str, surname: str, position: str, salary: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "salary": salary,
            "bonus": bonus
        }


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} |'

    def get_total_income(self):
        return f'Total income : {sum(self._income.values())}'

    def get_position(self):
        return f'{self.position} |'


stas = Position("Stanislav", "Livshits", "COO", 18000, 800)
print(stas.get_full_name(), stas.get_position(), stas.get_total_income())

dan = Position("Dan", "Krigman", "Project manager", 14500, 5000)
print(dan.get_full_name(), dan.get_position(), dan.get_total_income())