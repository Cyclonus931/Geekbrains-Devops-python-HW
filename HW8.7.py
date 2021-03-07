# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    real: float
    indeterminate: float

    def __init__(self, real: float, indeterminate: float):
        self.real = real
        self.indeterminate = indeterminate

    def __add__(self, other: 'ComplexNumber'):
        r1 = self.real + other.real
        i1 = self.indeterminate + other.indeterminate
        return f"({r1}{'+'if i1>0 else ''}{i1}i)"

    def __mul__(self, other: 'ComplexNumber'):
        r1 = self.real * other.real
        i1 = self.real * other.indeterminate
        i2 = self.indeterminate * other.real
        i3 = self.indeterminate * other.indeterminate

        real = r1
        indeterminate = i1 + i2 + i3

        return f"({real}{f'*{indeterminate}i' if indeterminate > 0 else f'*({indeterminate}i)'})"


first = ComplexNumber(2, 14)
second = ComplexNumber(5, -25.3)

print(first + second)
print(first * second)
