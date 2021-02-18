# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

while True:
    with open("HW5.1.txt", "a+") as my_txt_file:
        data_entering = input("Please enter some data or press Enter to finish >>> ")
        if data_entering == "":
            break
        else:
            my_txt_file.writelines(f'{data_entering}\n')
