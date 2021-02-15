# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
# а) итератор, генерирующий целые числа, начиная с указанного
my_cycle_list = int(input("Enter start number"))
number_of_cycles = int(input("Enter last number"))
for cycle in count(my_cycle_list):
    if cycle > number_of_cycles:
        break
    else:
        print(cycle)
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
my_cycle_list = input("Enter the list >>> ")
number_of_cycles = int(input("Enter number of cycles >>> "))
counter = 1

for my_cycle in cycle([my_cycle_list]):
    if counter > number_of_cycles:
        break
    else:
        print(my_cycle)
        counter += 1
