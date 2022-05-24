"""
методы для форматирования элементов списка по строкам

"""
import config_reader

# config
config = config_reader.read_config()
number_of_characters = int(config.get("string_terminator"))


# очищаю пробел перед и после строки
def line_cleaner(my_string):
    my_string_list = my_string.split(' ')
    my_string_list[len(my_string_list) - 1] = ''
    while my_string_list.count('') > 0:
        my_string_list.remove('')
    my_string = ' '.join(my_string_list)
    return my_string


# удаляю элементы списка равные: '', ' ', '  '
def space_cleaner(array):
    while array.count('') > 0:
        array.remove('')

    while array.count(' ') > 0:
        array.remove(' ')

    while array.count('  ') > 0:
        array.remove('  ')
    return array


"""
разделяю каждый элемент списка (список абзацев), т.е. 
абзац на количество символов
"""


def line_separator(line):
    word_list_with_spaces = line.split(' ')
    word_and_spaces_list = []
    for i in word_list_with_spaces:
        word_and_spaces_list.append(i)
        word_and_spaces_list.append(' ')

    string_items = []
    sp_pr_format = []
    for i in word_and_spaces_list:
        string_items.append(i)
        my_string = ''.join(string_items)
        if len(my_string) == number_of_characters:
            line_cleaner(my_string)
            sp_pr_format.append(my_string)
            string_items = []

        elif len(my_string) > number_of_characters:
            last_element = string_items.pop()
            my_string = line_cleaner(my_string)
            sp_pr_format.append(my_string)
            string_items = [last_element, ' ']

    if len(my_string) < number_of_characters:
        line_cleaner(my_string)
        sp_pr_format.append(my_string)

    space_cleaner(sp_pr_format)

    spr_fin = []
    for i in sp_pr_format:
        i = i.strip()
        spr_fin.append(i)

    return spr_fin
