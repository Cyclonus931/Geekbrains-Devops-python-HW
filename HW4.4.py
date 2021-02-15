# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
import random
start_list = []

for num in range(10):
    start_list.append(random.randrange(0, 10))

print(f'Start_list is >>> {start_list}')

unique_list = [el for el in start_list if start_list.count(el) == 1]

print(f'Unique numbers >>> {unique_list}')




