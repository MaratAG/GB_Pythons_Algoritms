"""
Задача 5.
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


start_code = 32
finish_code = 127

LEN_OF_STRING = 10

message = ''
lets_new_string = 0

for current_code in range(start_code, finish_code + 1):
    message += '{} - {}   '.format(current_code, chr(current_code))
    lets_new_string += 1

    if lets_new_string == LEN_OF_STRING:
        print(message)
        lets_new_string = 0
        message = ''

if lets_new_string != 0:
    print(message)
