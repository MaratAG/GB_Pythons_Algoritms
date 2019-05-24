"""
Задача 3.
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def get_sum_of_range(digit, iteration):
    sum_of_range = 0

    if iteration == 1:
        return digit

    sum_of_range += digit + get_sum_of_range(-digit / 2, iteration - 1)
    return sum_of_range


digit = 1
iteration = int(input('Введите количество элементов (n): '))

sum_of_range = get_sum_of_range(digit, iteration)
print('Сумма {} элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…: {}'.format(iteration, sum_of_range))
