"""
1 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random


def get_random_list(size, start, finish):
    """ Получаем одномерный массив из случайных целых чисел. """
    return [random.randint(start, finish) for _ in range(size)]


def bubble_sort(array_for_sort):
    """
    Сортируем массив методом пузырька (если за время прохождения внутреннего цикла не было произведено
    перестановок, то алгоритм сортировки завершается).
    """

    current_array = array_for_sort.copy()
    index = 1
    len_of_array_for_sort = len(current_array)
    array_needs_in_sort = True

    while index < len_of_array_for_sort and array_needs_in_sort:
        array_needs_in_sort = False
        for i in range(len_of_array_for_sort - index):
            if current_array[i] < current_array[i + 1]:
                current_array[i], current_array[i + 1] = current_array[i + 1], current_array[i]
                array_needs_in_sort = True
        index += 1

    return current_array


SIZE = 10
START_RANDOM = -100
FINISH_RANDOM = 99

array_for_sort = get_random_list(SIZE, START_RANDOM, FINISH_RANDOM)
sorted_array = bubble_sort(array_for_sort)

print('Исходный массив: {}'.format(array_for_sort))
print('Отсортированный массив: {}'.format(sorted_array))
