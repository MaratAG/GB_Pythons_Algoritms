"""
Задача 9.
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def count_sum_of_digits(digits):
    dec = 10
    sum_of_digits = 0
    len_digits = len(str(digits))

    if len_digits == 1:
        return digits

    dec_digits = dec ** (len_digits - 1)
    digit = digits // dec_digits
    sum_of_digits += digit + count_sum_of_digits(digits - digit * dec_digits)
    return sum_of_digits


winner_number = 0
sum_digits_of_winner_number = 0

count_of_number = int(input('Введите количество чисел, среди которых нужно найти максимальное по сумме цифр: '))

for _ in range(count_of_number):
    digits = int(input('Введите число: '))
    sum_of_digits = count_sum_of_digits(digits)
    if sum_of_digits > sum_digits_of_winner_number:
        winner_number = digits
        sum_digits_of_winner_number = sum_of_digits

print('Число, наибольшее по сумме цифр - {}, где сумма цифр {}.'.format(winner_number, sum_digits_of_winner_number))
