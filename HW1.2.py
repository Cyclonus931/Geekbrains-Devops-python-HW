# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

start_value = int(input('Hello! Please insert any time in seconds >>>  '))
hours = start_value // 3600
minutes = start_value % 3600 // 60
seconds = start_value % 3600 % 60
print(f'The time is : {hours}h:{minutes}m:{seconds}s')



