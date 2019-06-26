import sys


def main():
    KBYTES = 1024
    list_of_attributes = dir(test_module)
    list_of_attributes.reverse()

    total_size_of_memory = 0
    for item in list_of_attributes:
        if item[0] == '_':
            break
        size_of_attribute = eval('sys.getsizeof(test_module.{})'.format(item)) / KBYTES
        total_size_of_memory += size_of_attribute
        print('{}: {:.2f} килобайт'.format(item, size_of_attribute))

    print('Всего памяти, занятой переменными модуля: {:.2f} килобайт'.format(total_size_of_memory))


if __name__ == '__main__':
    params_of_start = sys.argv
    if len(params_of_start) == 2:
        import_module = params_of_start[1]
        exec('import {} as test_module'.format(import_module))
        main()
    else:
        print('Запустите программу в консоли, в качестве параметра укажите имя тестируемого модуля.')

"""
В качестве модулей для расчета занимаемой памяти взял 3 модуля из задания 4 'Оценка алгоритма' (модули 
прилагаются к заданию 6: les_6_test_1 (моя реализация), les_6_test_2 (реализация преподавателя), les_6_test_3 
(использование стандартных функций). 

МОДУЛЬ "les_6_test_1 (моя реализация)":
value: 0.07 килобайт
start_random: 0.03 килобайт
size: 0.03 килобайт
random: 0.08 килобайт
max_numbers: 0.05 килобайт
list_max_numbers: 0.07 килобайт
key_max_numbers: 0.03 килобайт
key: 0.03 килобайт
item: 0.03 килобайт
frequency_max_numbers: 0.03 килобайт
frequency_items_in_list: 36.10 килобайт
finish_random: 0.03 килобайт
current_list: 8493.62 килобайт
Всего памяти, занятой переменными модуля: 8530.18 килобайт

МОДУЛЬ "les_6_test_2 (реализация преподавателя)":
start_random: 0.03 килобайт
size: 0.03 килобайт
random: 0.08 килобайт
num: 0.03 килобайт
item: 0.03 килобайт
frequency: 0.03 килобайт
finish_random: 0.03 килобайт
counter: 36.10 килобайт
array: 8493.62 килобайт
Всего памяти, занятой переменными модуля: 8529.96 килобайт

МОДУЛЬ "les_6_test_3 (использование стандартных функций)":
start_random: 0.03 килобайт
size: 0.03 килобайт
random: 0.08 килобайт
frequency: 8.90 килобайт
finish_random: 0.03 килобайт
array: 8493.62 килобайт
Всего памяти, занятой переменными модуля: 8502.68 килобайт

ВЫВОДЫ
Как всегда, использование стандартных функций побеждает, а остальные два алгоритма делят второе место (конечно,
мой прожорливей :), но незначительно).

PS
Windows 10X64
Python 3.7.3

"""