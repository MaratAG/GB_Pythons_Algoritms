"""
Задача 7.
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""


def get_sum_of_range(number):
    sum_of_range = number
    if number == 1:
        return number
    sum_of_range += get_sum_of_range(number - 1)
    return sum_of_range


def get_result_of_formula(number):
    return int(number * (number + 1) / 2)


number = int(input('Введите любое натуральное число: '))
print('Сумма чисел ряда 1 .. {}: {}'.format(number, get_sum_of_range(number)))
print('Результат вычисления по формуле {0} * ({0} + 1) / 2: {1} '.format(number, get_result_of_formula(number)))
