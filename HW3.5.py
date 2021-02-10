# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_sum():
    total_sum = 0
    stop = 0

    while stop == 0:
        temp_sum = 0
        user_input = input('Please enter the numbers with space between them or q for exit >>> ').split()

        for arg in user_input:

            if arg == "q":
                stop = 1
                break
            else:
                try:
                    temp_sum = temp_sum + int(arg)
                except ValueError:
                    print("Wrong Value")
                    break

        total_sum = total_sum + temp_sum
        print(f'Your sum total >>> {total_sum}')


my_sum()
