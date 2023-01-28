#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в
# нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо
# запускать скрипт с параметрами.

import sys

function_obj, hours_worked_v, rate_per_hour_v, premium_v = sys.argv
print(function_obj)

def payroll_calculation(hours_worked, rate_per_hour, premium):
    try:
        print(f'Заработная плата сотрудника составляет {int(hours_worked) * int(rate_per_hour) + int(premium)}')
    except TypeError:
        print('Вы ввели недопустимое значение')

payroll_calculation(hours_worked_v, rate_per_hour_v, premium_v)