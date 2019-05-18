"""
Задача 9. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого).
"""

first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
third_number = float(input('Введите третье число: '))

middle_number = first_number

if first_number < second_number < third_number or third_number < second_number < first_number:
    middle_number = second_number
elif first_number < third_number < second_number or second_number < third_number < first_number:
    middle_number = third_number

print(' Среднее из введенных чисел: {}'.format(middle_number))
