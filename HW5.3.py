# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import statistics

with open("HW5.3.txt") as my_txt_file:
    low_salary = []
    salary = []
    for row in my_txt_file.readlines():
        salary_dict = {row.split()[0]: row.split()[1]}
        salary.append(float(row.split()[1]))
        if float(row.split()[1]) < 20000:
            low_salary.append(row.split()[0])

print(f'Employee which has salary lower then 20K  >>> {low_salary}')
print(f'Employees average salary >>> {statistics.mean(salary)}')