# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами

from sys import argv


def salary(work_hours, pay_per_hour, premium):
    return int(work_hours) * int(pay_per_hour) + int(premium)


work_hours, pay_per_hour, premium = argv

print(salary(work_hours, pay_per_hour, premium))
