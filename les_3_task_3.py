"""
Задача 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


import random


def get_random_list(size, start, finish):
    return [random.randint(start, finish) for _ in range(size)]


SIZE = 10
START_RANDOM = 1
FINISH_RANDOM = 1000

index_min = 0
index_max = 0

current_list = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)

print('Исходный массив {}'.format(current_list))

for index in range(len(current_list)):
    index_min = index if current_list[index] < current_list[index_min] else index_min
    index_max = index if current_list[index] > current_list[index_max] else index_max

if index_min != index_max:
    current_list[index_min], current_list[index_max] = current_list[index_max], current_list[index_min]

print('Измененный массив {}'.format(current_list))
