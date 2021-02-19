# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translated_data = []
translate_dict = {
    "Zero": "Ноль",
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять"
}

with open("HW5.4.txt") as my_txt_file:
    for row in my_txt_file.readlines():
        key, value = row.split(' - ')
        translated_data.append(f'{translate_dict[key]} - {value}')


with open("HW5.4_new.txt", "w", encoding='utf8') as my_txt_file_new:
    my_txt_file_new.writelines(translated_data)
