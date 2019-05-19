"""
Задача 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
"""


number_of_digits = 3
number_for_task = int(input('Введите трехзначное число:'))
digits = abs(number_for_task)

if len(str(digits)) == number_of_digits:
    first_digit = digits // 100
    second_digit = (digits - first_digit * 100) // 10
    third_digit = digits - first_digit * 100 - second_digit * 10

    sum_of_digits = first_digit + second_digit + third_digit
    multiply_of_digits = first_digit * second_digit * third_digit

    print('Сумма цифр числа: {}'.format(sum_of_digits))
    print('Произведение цифр числа: {}'.format(multiply_of_digits))
else:
    print('Число не отвечает условиям задачи')
