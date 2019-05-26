"""
Задача 1.
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""


def calculate_operation(first_number, second_number, sign_of_operation, code_of_exit):
    """ Выполнить операцию калькулятора. """
    message = 'Ошибка при выполнении операции'
    if sign_of_operation != code_of_exit:
        if (sign_of_operation == '+' or sign_of_operation == '-' or sign_of_operation == '*'
        or (sign_of_operation == '/' and second_number != '0')):
            command_of_python = first_number + sign_of_operation + second_number
            message = eval(command_of_python)

        if sign_of_operation == '/' and second_number == '0':
            message = 'Деление на ноль!'
    else:
        message = 'Выполнение программы закончено.'

    return message


sign_of_operation = ''
code_of_exit = '0'

while sign_of_operation != code_of_exit:
    first_number, sign_of_operation, second_number = (input('Введите числа и знак операции '
                                                            '(1-е число, знак, 2-е число)').split())
    message = calculate_operation(first_number, second_number, sign_of_operation, code_of_exit)
    print(message)
