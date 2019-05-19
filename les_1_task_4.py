"""
Задача 4.
Написать программу, которая генерирует в указанных пользователем границах:
● случайное целое число,
● случайное вещественное число,
● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""


import random


int_start, int_finish = map(int, input('Введите границы для генерации случайного целого числа: ').split())
float_start, float_finish = map(float, input('Введите границы для генерации случайного вещественного числа: ').split())
alpha_start, alpha_finish = map(ord, input('Введите границы для генерации случайного символа алфавита (a - z): ').split())

random_int = random.randint(int_start, int_finish)
random_float = random.uniform(float_start, float_finish)
random_alpha = chr(random.randint(alpha_start, alpha_finish))

print('Случайное целое число: {}'.format(random_int))
print('Случайное вещественное число: {0:.3f}'.format(random_float))
print('Случайный символ алфавита (a - z): {}'.format(random_alpha))
