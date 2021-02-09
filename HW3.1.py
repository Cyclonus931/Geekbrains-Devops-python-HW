# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divisor):
    return dividend / divisor


try:
    print(f'{division(int(input("Enter the dividend >>>")), int(input("Enter the divisor >>>")))}')
except ZeroDivisionError:
    print("cannot be divided by 0")
except ValueError:
    print('Value error')
