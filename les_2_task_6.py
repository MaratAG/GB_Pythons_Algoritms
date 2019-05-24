"""
Задача 6.
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
"""

import random


START_NUMBER = 0
FINISH_NUMBER = 100
NUMBER_OF_ATTEMPTS = 10

hidden_number = random.randint(START_NUMBER, FINISH_NUMBER)

current_attempt = 1
while current_attempt <= NUMBER_OF_ATTEMPTS:
    current_number = int(input('Попытка {}. Введите число:'.format(current_attempt)))
    if current_number == hidden_number:
        print('Угадали!')
        break
    elif current_number > hidden_number:
        print('Загаданное число меньше {}'.format(current_number))
    else:
        print('Загаданное число больше {}'.format(current_number))
    current_attempt += 1

if current_attempt > NUMBER_OF_ATTEMPTS:
    print('Попытки закончились. Загаданное число: {}'.format(hidden_number))
