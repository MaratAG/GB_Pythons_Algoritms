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
sum_of_range = get_sum_of_range(number)
result_of_formula = get_result_of_formula(number)

print('Сумма чисел ряда 1 .. {}: {}'.format(number, sum_of_range))
print('Результат вычисления по формуле {0} * ({0} + 1) / 2: {1} '.format(number, result_of_formula))
print('Равенство выполняется: {}'.format(sum_of_range == result_of_formula))
