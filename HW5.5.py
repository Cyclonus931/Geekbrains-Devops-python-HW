# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


import random
start_list = []

for num in range(10):
    start_list.append(random.randrange(0, 100))


with open("HW5.5.txt", "w") as my_txt_file:
    my_txt_file.write(" ".join(map(str, start_list)))


with open("HW5.5.txt") as my_txt_file_new:
    final_list = my_txt_file_new.read().split()
    print(sum(int(number) for number in final_list))
