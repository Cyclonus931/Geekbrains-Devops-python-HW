# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Date:
    day: int
    month: int
    year: int

    def __init__(self, date_str: str):
        numbers = Date.int_numbers(date_str)
        self.check_numbers(numbers)

        self.day, self.month, self.year = numbers

    @classmethod
    def int_numbers(cls, date_str: str) -> list:
        return [int(number) for number in date_str.split('-')]

    @staticmethod
    def check_numbers(numbers: list):
        d, m, y = numbers
        if m == 2:
            assert 1 <= d <= 28, "The is no such day in this month"
        elif m == 4 or m == 6 or m == 9 or m == 11:
            assert 1 <= d <= 30, "The is no such day in this month"
        else:
            assert 1 <= d <= 31, "The is no such day in this month"

        assert 1 <= m <= 12, "Wrong month format"
        assert 0 <= y <= 3000, "Wrong year format"


date = Date('31-01-2020')
# date = Date('24-00-2020')  # error
# date = Date('31-02-2020')  # error
# date = Date('31-04-2020')  # error
