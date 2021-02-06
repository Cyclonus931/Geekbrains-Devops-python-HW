# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
# название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры: [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример: {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

num = 1
goods_list = []

while True:
    goods_dict = {'Name': input("Enter good name").capitalize(),
                  'Price': int(input("Enter good price")),
                  'Quantity': int(input("Enter good quantity")),
                  'Unit': input("Enter good unit ").capitalize()
                  }

    goods_tuple = (num, goods_dict)
    goods_list.append(goods_tuple)
    num += 1
    print(goods_list)
    question = input('Press "A" for analytics , or "Enter" to continue').lower()

    if question == "a":
        analytics_dict = {
            'Name': [],
            'Price': [],
            'Quantity': [],
            'Unit': set()
        }

        for string, item in goods_list:
            analytics_dict['Name'].append(item['Name'])
            analytics_dict['Price'].append(item['Price'])
            analytics_dict['Quantity'].append(item['Quantity'])
            analytics_dict['Unit'].add(item['Unit'])

        print(analytics_dict)
        exit()
