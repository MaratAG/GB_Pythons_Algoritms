"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random


def get_random_matrix(size_rows, size_columns, start, finish):
    """ Получаем матрицу размерности size_rows Х size_columns из случайных целых чисел. """
    return [[random.randint(start, finish) for _ in range(size_columns)] for _ in range(size_rows)]


def get_min_items_of_columns(matrix):
    """ Получаем индексы минимальных элементов столбцов."""
    min_items_of_columns = {}
    for j in range(SIZE_COLUMNS):
        min_element = matrix[0][j]
        min_indexes = (0, j)
        for i in range(1, SIZE_ROWS):
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_indexes = (i, j)
        if min_element in min_items_of_columns.keys():
            min_items_of_columns[min_element].append(min_indexes)
        else:
            min_items_of_columns[min_element] = [min_indexes]

    return min_items_of_columns


SIZE_ROWS = 5
SIZE_COLUMNS = 4
START_RANDOM = -10
FINISH_RANDOM = 10

matrix = get_random_matrix(SIZE_ROWS, SIZE_COLUMNS, START_RANDOM, FINISH_RANDOM)

print('Исходная матрица:')
for row in matrix:
    print(row)

min_items_of_columns = get_min_items_of_columns(matrix)

for key, value in min_items_of_columns.items():
    max_item = key
    break

for key, value in min_items_of_columns.items():
    max_item = key if key > max_item else max_item

print('Максим-ьный {} среди минимальных элементов столбцов матрицы '
      'находится по индексам: {}'.format(max_item, min_items_of_columns[max_item]))
