"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

import random


def get_random_matrix(size_rows, size_columns, start, finish):
    """ Получаем матрицу размерности size_rows Х size_columns из случайных целых чисел. """
    return [[random.randint(start, finish) for _ in range(size_columns)] for _ in range(size_rows)]


SIZE_ROWS = 5
SIZE_COLUMNS = 4
START_RANDOM = -10
FINISH_RANDOM = 10

matrix = get_random_matrix(SIZE_ROWS, SIZE_COLUMNS - 1, START_RANDOM, FINISH_RANDOM)

for row in matrix:
    sum_elements_of_row = 0
    for item in row:
        sum_elements_of_row += item
    row.append(sum_elements_of_row)
    print(row)
