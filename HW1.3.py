# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Insert the number >>> '))
value = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(f'{n} + {str(n) + str(n)} + {int(str(n) + str(n) + str(n))} = {value}')
