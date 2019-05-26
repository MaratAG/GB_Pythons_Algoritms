"""
Задача 2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def its_odd(digit):
    return 0 if digit % 2 == 0 else 1


def count_odd(digits):
    dec = 10
    counter_odd = 0
    len_digits = len(str(digits))

    if len_digits == 1:
        return its_odd(digits)

    dec_digits = dec ** (len_digits - 1)
    digit = digits // dec_digits
    counter_odd += its_odd(digit) + count_odd(digits - digit * dec_digits)
    return counter_odd


digits = int(input('Введите натуральное число: '))

odd = count_odd(digits)
len_digits = len(str(digits))
even = len_digits - odd

print('В числе {} четных цифр {}, нечетных цифр {}'.format(digits, even, odd))
