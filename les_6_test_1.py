import random

size = 1000000
start_random = 1
finish_random = 1000

current_list = [random.randint(start_random, finish_random) for _ in range(size)]

frequency_items_in_list = {}
for item in current_list:
    if item in frequency_items_in_list.keys():
        frequency_items_in_list[item] += 1
    else:
        frequency_items_in_list[item] = 1

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

frequency_max_numbers, max_numbers = key_max_numbers, ', '.join(map(str, list_max_numbers))
