"""
Задача 2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5, если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""


import random


def get_random_list(size, start, finish):
    return [random.randint(start, finish) for _ in range(size)]


SIZE = 10
START_RANDOM = 1
FINISH_RANDOM = 1000

current_list = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)
result_list = [index for index in range(len(current_list)) if current_list[index] % 2 == 0]

print('Исходный массив {}'.format(current_list))
print('Массив индексов четных элементов исходного массива {}'.format(result_list))
