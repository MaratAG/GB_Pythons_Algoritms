"""
Задача 8. Определить, является ли год, который ввел пользователь, високосным или не високосный.
"""

message = 'Не високосный'

year = int(input('Введите год: '))

if year % 100 == 0:
    if year % 400 == 0:
        message = 'Високосный'
else:
    if year % 4 == 0:
        message = 'Високосный'

print('Год {} - {}'.format(year, message))
