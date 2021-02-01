# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

a = int(input("Insert a positive integer >>> "))
max_dig = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > max_dig:
        max_dig = a % 10
    if a > 9:
        continue
    else:
        print("Maximum digit in number >>>  ", max_dig)
        break
