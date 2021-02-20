# Создать вручную и заполнить строками текстовый файл,в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
main_list = []

with open("HW5.7.txt") as my_txt_file:
    companies_profit = {}
    profit_list = []
    for company in my_txt_file.readlines():
        name, form, income, outcome = company.split()
        companies_profit[name] = (float(income) - float(outcome))
        if companies_profit[name] >= 0:
            profit_list.append(companies_profit[name])

    main_list.append(companies_profit)
    main_list.append({"average_profit": sum(profit_list) / len(profit_list)})

with open("HW5.7.json", "w") as my_json_file:
    json.dump(main_list, my_json_file)



