# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = float(input('Please enter your monthly income >>> '))
outcome = float(input('Please enter your monthly outcome >>> '))
difference = float(income - outcome)
profitability = float(difference / income * 100)
if income > outcome:
    print(f'Your monthly profit is >>> {difference:.2f}$')
    print(f'Your monthly profitability is >>> {profitability:.2f}%')
    staff = int(input('Please enter the number of your employees >>> '))
    print(f'Your profit per employee >>> {difference / staff:.2f}$')
elif income == outcome:
    print('Your income and outcome founds are equal')
else:
    print(f'your monthly loss >>> {difference:.2f}$')
