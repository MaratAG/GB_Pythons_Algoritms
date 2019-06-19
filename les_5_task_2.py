"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def get_hash_dec():
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15}


def get_hash_hex():
    return {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
    '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}


def get_normalize_number(hex_number, max_of_len):
    while len(hex_number) < max_of_len:
        hex_number.appendleft('0')

    return hex_number


def sum_hex_digits(dec_A, dec_B):
    global next_dec
    sum_dec = hash_dec[next_dec] + hash_dec[dec_A] + hash_dec[dec_B]
    next_dec = '0'
    if sum_dec > 15:
        sum_dec -= 16
        next_dec = '1'
    result_of_sum.appendleft(hash_hex[str(sum_dec)])


def sum_of_hex(dec_A, dec_B):
    for index in range(max_of_len - 1, -1, -1):
        dec_A = number_A[index]
        dec_B = number_B[index]
        sum_hex_digits(dec_A, dec_B)

    if next_dec == '1':
        result_of_sum.appendleft(hash_dec[next_dec])


hash_dec = get_hash_dec()
hash_hex = get_hash_hex()
result_of_sum = deque()
next_dec = '0'

number_A = deque(input('Введите первое шестандцатеричное число: ').upper())
number_B = deque(input('Введите второе шестандцатеричное число: ').upper())

max_of_len = max(len(number_A), len(number_B))
number_A = get_normalize_number(number_A, max_of_len)
number_B = get_normalize_number(number_B, max_of_len)

sum_of_hex(number_A, number_B)

print('{} + {} = {}'.format(''.join(number_A), ''.join(number_B), ''.join(result_of_sum)))
