"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random


def get_random_list(size, start, finish):
    """ Получаем одномерный массив из случайных целых чисел. """
    return [random.randint(start, finish) for _ in range(size)]


def get_min_item_in_set(uniq_items):
    """ Находим минимальный элемент множества. """
    for item in uniq_items:
        min_item = item
        break

    for item in uniq_items:
        min_item = item if item < min_item else min_item
    return min_item


def get_min_runnerdown_item(current_list):
    """ Находим минимальное и ближайшее к минимальному значения множества. """
    min_item = current_list[0]

    uniq_items = set(current_list)
    min_item = get_min_item_in_set(uniq_items)

    uniq_items.remove(min_item)
    runnerdown_item = get_min_item_in_set(uniq_items)

    return min_item, runnerdown_item


def get_indexes_with_item(min_item):
    """ Получаем список индексов элементов с необходимым нам значением. """
    indexes = []
    global count_iteration
    for index, item in enumerate(current_list):
        if count_iteration == COUNT_MIN_ELEMENTS:
            break
        if item == min_item:
            indexes.append(index)
            count_iteration += 1
    return indexes


SIZE = 10
START_RANDOM = -10
FINISH_RANDOM = 10
COUNT_MIN_ELEMENTS = 2

count_iteration = 0
min_indexes = []
runner_down_indexes = []

current_list = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)
min_item, runner_down_item = get_min_runnerdown_item(current_list)

min_indexes = get_indexes_with_item(min_item)
runner_down_indexes = get_indexes_with_item(runner_down_item)

if len(min_indexes) > 1:
    runner_down_item = min_item

print('Исходный список: {}'.format(current_list))
print('Два наименьших по значению элемента в списке: {} и {} '.format(min_item, runner_down_item))
print('Индексы элементов со значением {}: {}'.format(min_item, ', '.join(map(str, min_indexes))))

if len(min_indexes) == 1:
    print('Индексы элементов со значением {}: {}'.format(runner_down_item, ', '.join(map(str, runner_down_indexes))))
