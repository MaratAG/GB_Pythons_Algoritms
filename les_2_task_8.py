"""
Задача 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def its_digit_for_count(digit):
    return 1 if digit == digit_for_count else 0


def count_occurrences_of_number(digits):
    dec = 10
    counter_occurences = 0
    len_digits = len(str(digits))

    if len_digits == 1:
        return its_digit_for_count(digits)

    dec_digits = dec ** (len_digits - 1)
    digit = digits // dec_digits
    counter_occurences += its_digit_for_count(digit) + count_occurrences_of_number(digits - digit * dec_digits)
    return counter_occurences


sum_counters_of_occurrences = 0
digit_for_count = int(input('Введите цифру, количество вхождений которой нужно посчитать: '))
count_of_number = int(input('Введите количество вводимых чисел для подсчета вхождений цифры: '))

for _ in range(count_of_number):
    digits = int(input('Введите число для подсчета вхождения цифры: '))
    sum_counters_of_occurrences += count_occurrences_of_number(digits)

print('Цифра {} встречается в последовательности {} раз.'.format(digit_for_count, sum_counters_of_occurrences))
