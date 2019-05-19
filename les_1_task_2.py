"""
Задача 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

number_a = 5
number_b = 6
number_of_bits = 2

operation_and = number_a & number_b
operation_or = number_a | number_b
operation_xor = number_a ^ number_b

operation_compliment_a = ~ number_a
operation_compliment_b = ~ number_b

bitwise_right_shift_a = number_a << number_of_bits
bitwise_left_shift_a = number_a >> number_of_bits

print('Логическая операция "И": {}'.format(operation_and))
print('Логическая операция "ИЛИ": {}'.format(operation_or))
print('Логическая операция "Исключительное ИЛИ": {}'.format(operation_xor))
print('Комплиментарный оператор, число a: {}'.format(~ number_a))
print('Комплиментарный оператор, число b : {}'.format(~ number_b))
print('Побитовый сдвиг вправо, число a  на {} знака: {}'.format(number_of_bits, number_a >> number_of_bits))
print('Побитовый сдвиг влево, число a на {} знака: {}'.format(number_of_bits, number_a << number_of_bits))
