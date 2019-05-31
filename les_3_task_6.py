"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать
"""

import random


def get_random_list(size, start, finish):
    return [random.randint(start, finish) for _ in range(size)]


def get_minmax_index(current_list):
    min_index = max_index = 0
    for index, value in enumerate(current_list):
        min_index = index if value < current_list[min_index] else min_index
        max_index = index if value > current_list[max_index] else max_index

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    return min_index, max_index


SIZE = 10
START_RANDOM = -100
FINISH_RANDOM = 100

current_list = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)

min_index, max_index = get_minmax_index(current_list)

sum_elements = 0
for index in range(min_index + 1, max_index): sum_elements += current_list[index]

print('Исходный список: {}'.format(current_list))
print('Сумма элементов между элементов с индексами {} и {} равна: {}'.format(min_index, max_index, sum_elements))
