"""
Задача 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
в диапазоне от 2 до 9.
"""


def get_empty_multiplicity_data():
    return {key: 0 for key in range(START_MULTIPLICITY, FINISH_MULTIPLICITY + 1)}


START = 2
FINISH = 99

START_MULTIPLICITY = 2
FINISH_MULTIPLICITY = 9

multiplicity_result = get_empty_multiplicity_data()

print('Дан список натуальных чисел от {} до {}, где:'.format(START, FINISH))

for number in range(START, FINISH + 1):
    for item in multiplicity_result:
        multiplicity_result[item] += 1 if number % item == 0 else 0

for key, value in multiplicity_result.items():
    print('- цифре {} кратно {} чисел'.format(key, value))
