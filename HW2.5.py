# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


my_list = [7, 5, 3, 3, 2]
while True:
    user_input = input('Please enter your rating number >>> ')
    if not user_input.isdigit():
        print('Wrong entering')
    else:
        rating = int(user_input)
        my_list.append(rating)
        my_list.sort(reverse=True)
        print(my_list)
        exit()  # Если нужно повторять запрос, то просто стираем exit



