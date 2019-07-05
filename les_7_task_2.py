"""
2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def get_random_list(size, start, finish):
    """ Получаем одномерный массив из случайных вещественных чисел. """
    current_finish = finish - .00000000000001 # :)
    current_start = current_finish if start == finish else start
    return [random.uniform(current_start, current_finish) for _ in range(size)]


def merge_sorted_arrays(first_half, second_half):
    """
    Слияние упорядоченных массива в один с использованием буфера.
    """
    buffer = []
    index_of_first_half = 0
    index_of_second_half = 0

    len_of_first_half = len(first_half)
    len_of_second_half = len(second_half)

    while index_of_first_half < len_of_first_half and index_of_second_half < len_of_second_half:
        if first_half[index_of_first_half] <= second_half[index_of_second_half]:
            buffer.append(first_half[index_of_first_half])
            index_of_first_half += 1
        else:
            buffer.append(second_half[index_of_second_half])
            index_of_second_half += 1

    while index_of_second_half < len_of_second_half:
        buffer.append(second_half[index_of_second_half])
        index_of_second_half += 1

    while index_of_first_half < len_of_first_half:
        buffer.append(first_half[index_of_first_half])
        index_of_first_half += 1

    return buffer


def merge_sort(array_for_sort):
    """
    Сортируем массив методом слияния.
    """
    len_of_array_for_sort = len(array_for_sort)
    if len_of_array_for_sort <= 1:
        return array_for_sort

    mediana = len_of_array_for_sort // 2
    first_half = merge_sort(array_for_sort[:mediana])
    second_half = merge_sort(array_for_sort[mediana:])
    merged_list = merge_sorted_arrays(first_half, second_half)

    return merged_list


SIZE = 5
START_RANDOM = 0
FINISH_RANDOM = 50

array_for_sort = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)
sorted_array = merge_sort(array_for_sort.copy())

print('Исходный массив: {}'.format(array_for_sort))
print('Отсортированный массив: {}'.format(sorted_array))
