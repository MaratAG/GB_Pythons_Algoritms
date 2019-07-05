"""
13 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random
from collections import Counter


def get_random_list(size, start, finish):
    """ Получаем одномерный массив из случайных целых чисел. """
    return [random.randint(start, finish) for _ in range(size)]


def get_mediana(array, very_big_element):
    """Получаем медиану с использованием гистограммы."""
    half_of_array = (len(array) - 1) / 2
    overflow_under_half = 0
    used_elements = []

    count_values = dict(Counter(array))

    while not overflow_under_half > half_of_array:
        min_value = very_big_element
        for key in count_values.keys():
            if min_value > key and not (key in used_elements):
                min_value = key

        overflow_under_half += count_values[min_value]
        used_elements.append(min_value)

    return min_value


m = 10000
SIZE = 2 * m + 1
START_RANDOM = 0
FINISH_RANDOM = 100

array = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)
mediana = get_mediana(array, FINISH_RANDOM + 1)

print('Исходный массив: {}'.format(array))
print('Медиана: {}'.format(mediana))
