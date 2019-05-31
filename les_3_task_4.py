"""
Задача 4. Определить, какое число в массиве встречается чаще всего.
"""


import random


def get_random_list(size, start, finish):
    return [random.randint(start, finish) for _ in range(size)]


def get_frequency_items(current_list):
    frequency = {}
    for item in current_list:
        if item in frequency.keys():
            frequency[item] += 1
        else:
            frequency[item] = 1

    return frequency


def get_list_max_numbers(frequency_items_in_list):
    max_numbers = {}
    for key, value in frequency_items_in_list.items():
        if value in max_numbers.keys():
            max_numbers[value].append(key)
        else:
            max_numbers[value] = [key]

    key_max_numbers = 0
    list_max_numbers = []

    for key, value in max_numbers.items():
        if key > key_max_numbers:
            key_max_numbers = key
            list_max_numbers = value

    return key_max_numbers, ', '.join(map(str, list_max_numbers))


SIZE = 10
START_RANDOM = 1
FINISH_RANDOM = 10

current_list = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)
frequency_items_in_list = get_frequency_items(current_list)
frequency_max_numbers, max_numbers = get_list_max_numbers(frequency_items_in_list)

print('Исходный список: {}'.format(current_list))
print('Число(а) {} встречается(ются) с максимальной частотой {}'.format(max_numbers, frequency_max_numbers))
