"""
Задача 4.1: Оценить сложность 3 вариантов реализации задачи:
Задача 3.4. Определить, какое число в массиве встречается чаще всего.
"""


import cProfile
import random
from collections import Counter


# ОБЩИЕ ФУНКЦИИ
def get_random_list(size, start, finish):
    return [random.randint(start, finish) for _ in range(size)]


# ФУНКЦИИ ВАРИАНТА #1 АЛГОРИТМА
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


def execute_algorithm_1(size, start_random, finish_random, timing=False):
    current_list = get_random_list(size, start_random, finish_random)

    frequency_items_in_list = get_frequency_items(current_list)
    frequency_max_numbers, max_numbers = get_list_max_numbers(frequency_items_in_list)

    if timing is False:
        print('Исходный список: {}'.format(current_list))
        print('Число(а) {} встречается(ются) с максимальной частотой {}'.format(max_numbers, frequency_max_numbers))


# ФУНКЦИИ ВАРИАНТА #2 АЛГОРИТМА
def execute_algorithm_2(size, start_random, finish_random, timing=False):
    array = get_random_list(size, start_random, finish_random)

    counter = dict()
    frequency = 1
    num = None

    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    if timing is False:
        print('Исходный список: {}'.format(array))
        if num is not  None:
            print(f'Число {num} встречается {frequency} раз (а)')
        else:
            print('Все элементы уникальны')


# ФУНКЦИИ ВАРИАНТА #3 АЛГОРИТМА
def execute_algorithm_3(size, start_random, finish_random, timing=False):
    array = get_random_list(size, start_random, finish_random)
    frequency = list(dict(Counter(array)).items())
    frequency.sort(key=lambda i: i[1], reverse=True)

    if timing is False:
        print('Исходный список: {}'.format(array))
        if len(frequency) != len(array):
            print(f'Число {frequency[0][0]} встречается {frequency[0][1]} раз (а)')
        else:
            print('Все элементы уникальны')


# МОДУЛЬ ИНИЦИАЛИЗАЦИИ
def main():
    size = 1000000
    start_random = 1
    finish_random = 1000

    execute_algorithm_1(size, start_random, finish_random, True)

    execute_algorithm_2(size, start_random, finish_random, True)

    execute_algorithm_3(size, start_random, finish_random, True)


if __name__ == '__main__':
    cProfile.run("main()")


"""
Были проведены тесты по оценке скорости и сложности 3-х вариантов алгоритмов решения задачи 4 к уроку 3:
    1. Алгоритм, которым задача была решена мной;
    2. Алгоритм, который был предложен для решения задачи преподавателем;
    3. Алгоритм с использованием Counter() и типовых функций сортировки.
    
А. ОЦЕНКА СКОРОСТИ РАБОТЫ АЛГОРИТМОВ
Метод оценки: Использование модуля timeit (запуск через консоль);
Параметры оценки: Для каждого из алгоритмов была выполнена серия из 6 тестов, где:
    - размер массива = 1000
    - размер массива = 10000
    - размер массива = 100000
    - размер массива = 500000
    - размер массива = 750000
    - размер массива = 1000000

РЕЗУЛЬТАТЫ ВЫПОЛНЕНИЯ ТЕСТА (А):
Алгоритм 1:
- 100 loops, best of 5: 1.69 msec per loop
- 100 loops, best of 5: 13.9 msec per loop
- 100 loops, best of 5: 146 msec per loop
- 100 loops, best of 5: 740 msec per loop
- 100 loops, best of 5: 1.11 sec per loop
- 100 loops, best of 5: 1.49 sec per loop

Алгоритм 2:
- 100 loops, best of 5: 1.44 msec per loop
- 100 loops, best of 5: 14 msec per loop
- 100 loops, best of 5: 143 msec per loop
- 100 loops, best of 5: 768 msec per loop
- 100 loops, best of 5: 1.2 sec per loop
- 100 loops, best of 5: 1.53 sec per loop

Алгоритм 3:    
- 100 loops, best of 5: 1.36 msec per loop
- 100 loops, best of 5: 12.3 msec per loop
- 100 loops, best of 5: 127 msec per loop
- 100 loops, best of 5: 644 msec per loop
- 100 loops, best of 5: 991 msec per loop
- 100 loops, best of 5: 1.33 sec per loop

Б. ОЦЕНКА ПРОИЗВОДИТЕЛЬНОСТИ РАБОТЫ АЛГОРИТМОВ
n = 1000:
        1    0.000    0.000    0.007    0.007 les_4_task_1.py:47(execute_algorithm_1)
        1    0.000    0.000    0.005    0.005 les_4_task_1.py:59(execute_algorithm_2)
        1    0.000    0.000    0.005    0.005 les_4_task_1.py:84(execute_algorithm_3)
        
      630    0.000    0.000    0.000    0.000 les_4_task_1.py:87(<lambda>) # Алгоритм 3
     1633    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects} # Алгоритм 1 
      622    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} # Алгоритм 2        
        

n = 10000;
        1    0.000    0.000    0.039    0.039 les_4_task_1.py:47(execute_algorithm_1)
        1    0.006    0.006    0.055    0.055 les_4_task_1.py:59(execute_algorithm_2)
        1    0.001    0.001    0.052    0.052 les_4_task_1.py:84(execute_algorithm_3)
        
     1000    0.000    0.000    0.000    0.000 les_4_task_1.py:87(<lambda>) # Алгоритм 3
    11000    0.001    0.000    0.001    0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
      979    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} # Алгоритм 2           

n = 100000:
        1    0.000    0.000    0.363    0.363 les_4_task_1.py:47(execute_algorithm_1)
        1    0.023    0.023    0.233    0.233 les_4_task_1.py:59(execute_algorithm_2)
        1    0.001    0.001    0.194    0.194 les_4_task_1.py:84(execute_algorithm_3)
        
     1000    0.000    0.000    0.000    0.000 les_4_task_1.py:87(<lambda>) # Алгоритм 3
   101000    0.005    0.000    0.005    0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
      944    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} # Алгоритм 2
      
n = 500000;
        1    0.000    0.000    1.340    1.340 les_4_task_1.py:47(execute_algorithm_1)
        1    0.108    0.108    1.061    1.061 les_4_task_1.py:59(execute_algorithm_2)
        1    0.004    0.004    0.958    0.958 les_4_task_1.py:84(execute_algorithm_3)
        
     1000    0.000    0.000    0.000    0.000 les_4_task_1.py:87(<lambda>) # Алгоритм 3
   501000    0.031    0.000    0.031    0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
      888    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} # Алгоритм 2            

n = 750000;
        1    0.000    0.000    1.728    1.728 les_4_task_1.py:47(execute_algorithm_1)
        1    0.186    0.186    1.544    1.544 les_4_task_1.py:59(execute_algorithm_2)
        1    0.005    0.005    1.503    1.503 les_4_task_1.py:84(execute_algorithm_3)
        
     1000    0.000    0.000    0.000    0.000 les_4_task_1.py:87(<lambda>) # Алгоритм 3     
   751000    0.043    0.000    0.043    0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
      861    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} # Алгоритм 2 

n = 1000000:
        1    0.000    0.000    2.544    2.544 les_4_task_1.py:47(execute_algorithm_1)
        1    0.236    0.236    2.145    2.145 les_4_task_1.py:59(execute_algorithm_2)
        1    0.007    0.007    1.990    1.990 les_4_task_1.py:84(execute_algorithm_3)  
        
     1000    0.000    0.000    0.000    0.000 les_4_task_1.py:87(<lambda>) # Алгоритм 3      
  1001000    0.060    0.000    0.060    0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
      847    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects} # Алгоритм 2

У алгоритма 1 производительность при увеличении объема обрабатываемых данных будет уменьшаться за счет того, 
что увеличивается доля времени, затрачиваемая на метод .keys() при работе со словарем:

1633 0.000 0.000 0.000 0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
11000 0.001 0.000 0.001 0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
101000 0.005 0.000 0.005 0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
501000 0.031 0.000 0.031 0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
751000 0.043 0.000 0.043 0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
1001000 0.060 0.000 0.060 0.000 {method 'keys' of 'dict' objects} # Алгоритм 1
Оптимизации данная часть кода алгоритма не подлежит, так как это и есть основа алгоритма :)

ВЫВОДЫ

Все три алгоритма решения задачи 3.4 имеют сложность О(n), что подтверждается графиками (линейная функция). 
Это свидетельствует о том, что все алгоритмы работают оптимально, так как в любом случае один "перебор" массива 
для выполнения задачи необходим.
Наиболее оптимальным, исходя из - производительности при росте обрабатываемых данных и простоте поддержки - 
является алгоритм с использованием типовых функций языка (подозреваю, что это связано с тем, что часть типовых модулей 
реализована на С и не требует интерпретации).

"""

