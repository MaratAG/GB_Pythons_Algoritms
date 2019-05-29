"""
Задача 4. Определить, какое число в массиве встречается чаще всего.
"""


import random


def get_random_list(size, start, finish):
    return [random.randint(start, finish) for _ in range(size)]


SIZE = 10
START_RANDOM = 1
FINISH_RANDOM = 1000

frequency = {}

current_list = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)

for item in current_list:
    if item in frequency.keys():
        frequency[item] += 1
    else:
        frequency[item] = 1

max_item = current_list[0]
max_frequency = frequency[max_item]
same_frequency = True

for key, value in frequency.items():
    if value > max_frequency:
        max_frequency = value
        max_item = key
        same_frequency = False
    elif value < max_frequency:
        same_frequency = False

print('Исходный массив {}'.format(current_list))

if same_frequency is True:
    print('Все элементы массива встречаются с одинаковой частотой.')
else:
    print('Число {} встречается в массиве чаще всего (частота - {})'.format(max_item, max_frequency))
