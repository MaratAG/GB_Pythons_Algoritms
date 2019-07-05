"""Определить количество различных подстрок с использованием хеш-функции. Задача: на вход
функции дана строка, требуется вернуть количество различных подстрок в этой строке.
"""
import hashlib


def get_count_uniq_strings(main_string):
    uniq_subs = set()
    len_of_main_string = len(main_string)
    for i in range(0, len_of_main_string):
        for j in range(len_of_main_string, 0, -1):
            sub_string = main_string[i:j]
            if sub_string != main_string and sub_string != '':
                uniq_subs.add(hashlib.sha1(sub_string.encode('utf-8')).hexdigest())
    return len(uniq_subs)


main_string = input('Введите строку: ')
print('Количество уникальных подстрок в строке: {}'.format(get_count_uniq_strings(main_string)))
