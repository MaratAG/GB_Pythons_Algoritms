"""
Задача 5.
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

first_symbol_alpha = 1
last_symbol_alpha = 26
difference_between_alpha_and_ascii = 96

first_symbol = input('Введите первую букву алфавита (a - z): ').strip()
second_symbol = input('Введите вторую букву алфавита (a - z): ').strip()

position_of_first_symbol = ord(first_symbol) - difference_between_alpha_and_ascii
position_of_second_symbol = ord(second_symbol) - difference_between_alpha_and_ascii

if (first_symbol_alpha <= position_of_first_symbol <= last_symbol_alpha and
first_symbol_alpha <= position_of_second_symbol <= last_symbol_alpha):
    distance_between_symbols = abs(position_of_second_symbol - position_of_first_symbol) - 1
    print('Позиция символа {} в алфавите: {}'.format(first_symbol, position_of_first_symbol))
    print('Позиция символа {} в алфавите: {}'.format(second_symbol, position_of_second_symbol))
    print('Между первым {} и вторым {} символами букв {}'.format(first_symbol, second_symbol, distance_between_symbols))
else:
    print('Введенные символы не соответствуют условиям задачи.')
