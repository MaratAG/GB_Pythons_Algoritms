"""
Задача 6.
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

first_symbol_alpha = 1
last_symbol_alpha = 26
difference_between_alpha_and_ascii = 96

number_of_symbol = int(input('Введите номер буквы в алфавите (1 - 26): '))

if first_symbol_alpha <= number_of_symbol <= last_symbol_alpha:
    symbol = chr(number_of_symbol + difference_between_alpha_and_ascii)
    print('Под номером {} буква {}'.format(number_of_symbol, symbol))
else:
    print('Введенный номер не соответствует условиям задачи.')
