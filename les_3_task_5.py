"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения
"""

import random


def get_random_list(size, start, finish):
    return [random.randint(start, finish) for _ in range(size)]


SIZE = 10
START_RANDOM = -10
FINISH_RANDOM = 10

max_negative_element = 0
max_negative_element_positions = []

current_list = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)

for index, item in enumerate(current_list):
    if (item < 0) and (max_negative_element == 0 or (max_negative_element < 0 and item >= max_negative_element)):
        if item == max_negative_element:
            max_negative_element_positions.append(index)
        else:
            max_negative_element = item
            max_negative_element_positions = [index]

str_max_negative_element_positions = ', '.join(map(str, max_negative_element_positions))

print('Исходный список: {}'.format(current_list))
print('Максимальный отрицательный элемент {}. '
      'Встречается на позициях: {}'.format(max_negative_element, str_max_negative_element_positions))
