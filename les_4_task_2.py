"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
"""

import cProfile
import math


def prime(position):
    current_position = 1
    current_number = FIRST_PRIME_NUMBER
    while current_position < position:
        current_number += 1
        if current_number % 2 != 0:
            its_prime = True
            for divider in range(FIRST_PRIME_NUMBER + 1, current_number):
                its_prime = False if current_number % divider == 0 else its_prime
            if its_prime is True:
                current_position += 1

    return current_number


def get_broad_of_seek_numbers(position):
    broad_of_seek_numbers = 10

    current_position = 0
    while current_position < position:
        current_position = round(broad_of_seek_numbers / math.log(broad_of_seek_numbers))
        broad_of_seek_numbers *= 10
    return broad_of_seek_numbers


def sieve(position):

    broad_of_seek_numbers = get_broad_of_seek_numbers(position)

    array_of_numbers = [0] * broad_of_seek_numbers
    for value in range(broad_of_seek_numbers):
        array_of_numbers[value] = value

    array_of_numbers[1] = 0

    current_position = 2
    while current_position < broad_of_seek_numbers:
        if array_of_numbers[current_position] != 0:
            no_prime_position = current_position * 2
            while no_prime_position < broad_of_seek_numbers:
                array_of_numbers[no_prime_position] = 0
                no_prime_position += current_position
        current_position += 1

    position_of_our_prime_number = 1
    current_number = FIRST_PRIME_NUMBER

    for index in range(3, len(array_of_numbers)):
        if array_of_numbers[index] != 0:
            if position_of_our_prime_number == position:
                break
            position_of_our_prime_number += 1
            current_number = array_of_numbers[index]

    return current_number


def main():
    position = 2000

    prime_position = prime(position)
    sieve_position = sieve(position)


FIRST_PRIME_NUMBER = 2

if __name__ == '__main__':
    cProfile.run("main()")

"""
Были проведены тесты по оценке скорости и сложности 2-х вариантов алгоритма решения задачи определения простого числа 
по позиции:

1. Алгоритм без использования решета Эратосфена;
2. Алгоритм с использованием решета Эратосфена.
А. ОЦЕНКА СКОРОСТИ РАБОТЫ АЛГОРИТМОВ Метод оценки: Использование модуля timeit (запуск через консоль); 
Параметры оценки: Для каждого из алгоритмов была выполнена серия из 5 тестов, где:

- loops = 100, позиция простого числа = 100
- loops = 100, позиция простого числа = 500
- loops = 100, позиция простого числа = 1000
- loops = 100, позиция простого числа = 1500
- loops = 100, позиция простого числа = 2000

Б. ОЦЕНКА ПРОИЗВОДИТЕЛЬНОСТИ РАБОТЫ АЛГОРИТМОВ Метод оценки: Использование модуля cProfile; 
Параметры оценки: Для каждого из алгоритмов была выполнена серия из 5 тестов, где n:

- позиция простого числа = 100
- позиция простого числа = 500
- позиция простого числа = 1000
- позиция простого числа = 1500
- позиция простого числа = 2000


РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ТЕСТА (А):
1. Алгоритм без использования решета Эратосфена:
100 loops, best of 5: 3.9 msec per loop
100 loops, best of 5: 237 msec per loop
100 loops, best of 5: 1.13 sec per loop
100 loops, best of 5: 2.93 sec per loop
100 loops, best of 5: 5.76 sec per loop

2. Алгоритм с использованием решета Эратосфена:
100 loops, best of 5: 3.38 msec per loop
100 loops, best of 5: 40 msec per loop
100 loops, best of 5: 47.3 msec per loop
100 loops, best of 5: 515 msec per loop


РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ТЕСТА (Б):
- позиция простого числа = 100:
 1    0.012    0.012    0.012    0.012 les_4_task_2.py:10(prime)
 1    0.008    0.008    0.008    0.008 les_4_task_2.py:35(sieve)
  
- позиция простого числа = 500:
1    0.313    0.313    0.313    0.313 les_4_task_2.py:10(prime)
1    0.057    0.057    0.057    0.057 les_4_task_2.py:35(sieve)

- позиция простого числа = 1000:
 1    1.334    1.334    1.334    1.334 les_4_task_2.py:10(prime)
 1    0.063    0.063    0.063    0.063 les_4_task_2.py:35(sieve)
   
- позиция простого числа = 1500;
1    3.421    3.421    3.421    3.421 les_4_task_2.py:10(prime)
1    0.527    0.527    0.527    0.527 les_4_task_2.py:35(sieve)

- позиция простого числа = 2000;
1    6.655    6.655    6.655    6.655 les_4_task_2.py:10(prime)
1    0.594    0.594    0.594    0.594 les_4_task_2.py:35(sieve)

ВЫВОДЫ
1. Для более точного определения графика для алгоритма Sieve нужно увеличить количество эксперементов и продолжить 
на 2500, 3000, 5000 и т.д., но у меня машина уже очень долго работает и на2500 для графика Prime, поэтому решил 
остановиться.
2. По полученным данным я предполагаю, что сложность алгоритма Prime - O(n^2), а алгоритма Sieve - O(n * log n). 
Конечно, алгоритм Sieve более предпочтителен для работы с большими выборками.

"""