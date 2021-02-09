# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(x, y):
    return x / y


dividend = int(input("Enter the dividend >>>"))
divisor = int(input("Enter the divisor >>>"))

try:
    print(division(dividend, divisor))
except ZeroDivisionError:
    print("cannot be divided by 0")
