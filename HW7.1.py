#  Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
#  который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    matrix_value_string: list

    def __init__(self, values: list):
        self.matrix_value_string = values

    def __add__(self, other: 'Matrix'):
        try:

            rows = len(self.matrix_value_string)  # 2
            items = len(self.matrix_value_string[0])  # 3
            new_matrix = [
                [
                    self.matrix_value_string[row][item] + other.matrix_value_string[row][item]
                    for item in range(items)
                ]
                for row in range(rows)
            ]
            return Matrix(new_matrix)
        except IndexError:
            print("One (or more) of your matrices doesn't have the same size as another one")
            exit()

    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace(',', '')
            for row in self.matrix_value_string
        )


a = Matrix([[1, 2, 3], [4, 5, 6]])

b = Matrix([[11, 22, 33], [44, 55, 66]])

c = Matrix([[111, 222, 333], [444, 555, 666]])

d = Matrix([[1111, 2222, 3333], [4444, 5555, 6666]])

res = a + b + c + d

print(res)
