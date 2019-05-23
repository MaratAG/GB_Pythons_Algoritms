"""
Задача 3.
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def get_reverse_digits(digits):
    dec = 10
    reverse_digits = 0
    len_digits = len(str(digits))

    if len_digits == 1:
        return digits * (dec ** (initial_len - 1))

    dec_digits = dec ** (len_digits - 1)
    digit = digits // dec_digits

    reverse_digits += (digit * (dec ** (initial_len - len_digits))
                       + get_reverse_digits(digits - digit * dec_digits))
    return reverse_digits


digits = int(input('Введите натуральное число: '))
initial_len = len(str(digits))
reverse_digits = get_reverse_digits(digits)

print('Введенное число {}  - обратное число {}'.format(digits, reverse_digits))
