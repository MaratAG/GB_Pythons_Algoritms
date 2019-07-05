"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter


class Node:
    """Класс, описывающий узел дерева."""
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node[value = {self.value}, left = {self.left}, right = {self.right}]'


def get_tree_of_symbols(dict_of_frequency):
    """Сформировать по словарю частоты повторения символов дерево с листьями-символами."""
    code_list = [(value, Node(key)) for key, value in dict_of_frequency.items()]

    while len(code_list) != 1:
        code_list = sorted(code_list, key=lambda x: (x[0]), reverse=True)
        right_element = code_list.pop()
        left_element = code_list.pop()
        new_node = Node('')
        new_node.left = left_element
        new_node.right = right_element
        code_list.append((left_element[0] + right_element[0], new_node))

    return code_list[0]


def get_code_lists_of_tree(node, total_code):
    """Сформировать по дереву словарь кодирования для подготовки архива."""
    if node[1].left is None and node[1].right is None:
        dict_of_coding[node[1].value] = total_code
        return None
    get_code_lists_of_tree(node[1].left, total_code + '1')
    get_code_lists_of_tree(node[1].right, total_code + '0')


def get_arc(code_string, dict_of_coding):
    """Получить архив строки с использованием полученного словаря кодирования."""
    result_string = ''
    for symbol in code_string:
        result_string += dict_of_coding[symbol]

    return result_string


dict_of_coding = dict()

code_string = input('Введите строку для архивирования: ')
dict_of_frequency = dict(Counter(code_string).most_common())

code_tree = get_tree_of_symbols(dict_of_frequency)
get_code_lists_of_tree(code_tree, '')


arc_string = get_arc(code_string, dict_of_coding)

print('Словарь для архивирования: {}'.format(dict_of_coding))
print('Полученная последовательность для архива: {}'.format(arc_string))
