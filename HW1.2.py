# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк

start_value = int(input('Hello! Please insert the any time in seconds >>>  '))
hours = start_value // 3600
minutes = start_value % 3600 // 60
seconds = start_value % 3600 % 60

print('The time is : {}h:{}m:{}s'.format('%02d' % hours, '%02d' % minutes, '%02d' % seconds))



