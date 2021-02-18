# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


with open("HW5.2.txt") as my_txt_file:
    separate_raw = [row.split() for row in my_txt_file.readlines()]
    row_counter = 1
    print(f'Number of rows >>> {len(separate_raw)}')
    for row in separate_raw:
        print(f'Number of words in {row_counter} row >>> {len(row)}')
        row_counter += 1

