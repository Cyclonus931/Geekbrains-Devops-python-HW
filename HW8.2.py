# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна обработать эту ситуацию и не завершиться ошибкой

class ZeroException(Exception):
    pass


def get_dividend():
    return int(input("Enter the dividend >>> "))


def get_divider():
    divider = int(input("Enter the divider >>> "))

    if divider == 0:
        raise ZeroException

    return divider


try:
    print(f"Result = {get_dividend() / get_divider()}")
except ZeroException:
    print("You cannot divide by 0")
