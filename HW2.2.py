# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = [input("Please insert first element ")]
element = input('Please insert next element')
element_count = 0
while element != "/":
    my_list.append(element)
    element = input('Please insert next element or press "/" if you finished')


for el in range(int(len(my_list) / 2)):
    my_list[element_count], my_list[element_count + 1] = my_list[element_count + 1], my_list[element_count]
    element_count += 2

print(my_list)
