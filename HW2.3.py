# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_dict = {'Winter': (1, 2, 12),
                'Spring': (3, 4, 5),
                'Summer': (6, 7, 8),
                'Autumn': (9, 10, 11)}
month_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

user_input = input('Please enter month number >>>')

if not user_input.isdigit():
    print('Wrong entering')
    exit()
    
month = int(user_input)

for key in seasons_dict.keys():
    if month in seasons_dict[key]:
        print(f'Dictionary result >>> {key}')


if month in month_list[0:3]:
    print('List result >>> Winter')
elif month in month_list[3:6]:
    print('List result >>> Spring')
elif month in month_list[6:9]:
    print('List result >>> Summer')
elif month in month_list[9:12]:
    print('List result >>> Autumn')
else:
    print(' Wrong number')
