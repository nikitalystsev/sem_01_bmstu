# Лысцев Н. Д. ИУ7-13Б
# Программа, которая с помощью меню обеспечивает работу
# с базой данных в текстовом файле
#
# Ввод
# меню из предложенных действий
# выбор номера пункта
#
# Вывод
# результат выполнения программы
import checks as ch


def menu():
    """
    Вывод меню
    """
    print("""
    1. Выбрать файл для работы
    2. Инициализировать базу данных
    3. Вывести содержимое базы данных
    4. Добавить запись в базу данных
    5. Поиск по одному полю
    6. Поиск по двум полям
    7. Выход из программы
     """)


def headlines():
    """
    Вывод заголовков базы данных
    """
    print(
        '1. Фамилия\n'
        '2. Имя\n'
        '3. Отчество\n'
        '4. Год рождения\n'
        '5. Школа\n'
        '6. Класс\n'
        '7. Учебная группа\n'
    )


def formatted_output(array_1: list, array_2: list):
    """
    Форматный вывод строки базы данных
    """
    for i in range(len(array_2)):
        array_2[i] = array_2[i].strip()
        array_2[i] += ' ' * (array_1[i] - len(array_2[i]))
    b = ' | '.join(array_2)
    return b


def list_of_maximum_lengths(file_name: str):
    """
    Функция возвращает список максимальных длин каждого поля базы данных
    """
    max_len = [0] * 7  # список максимальных длин каждого поля базы данных
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            string = file.readline()
            if not string:
                break
            string = list_split(string)
            print(string)
            for i in range(len(string)):
                if len(string[i]) > max_len[i]:
                    max_len[i] = len(string[i])
    return max_len


def item_number():
    """
    Возвращает номер пункта
    """
    while True:
        numb = ch.clever_input('Введите номер пункта меню: ')
        if numb < 1 or numb > 7:
            print('Неверный ввод! Номер пункта - целое число от 1 до 7. Пожалуйста, повторите ввод.')
        else:
            break
    return numb


def name_file():
    """
    Возвращает имя файла, введенное пользователем
    """
    name = input('Введите имя файла или полный путь к файлу: ')
    return name


def database_check(first_str):
    """
    Проверка на то, что база данных моя
    """
    my_database_headers = [
        "Фамилия",
        "Имя",
        "Отчество",
        "Год рождения",
        "Школа",
        "Класс",
        "Учебная группа",
    ]
    first_str = list_split(first_str)
    for i in range(len(first_str)):
        first_str[i] = first_str[i].strip()

    first_str[-1] = first_str[-1].rstrip('\n')

    if len(my_database_headers) == len(first_str):
        length = len(my_database_headers)
        for i in range(length):
            if my_database_headers[i] != first_str[i]:
                return False
        return True
    return False


def database_initialization(file_name: str):
    """
    Инициализация базы данных
    """
    if file_name is not None:
        try:
            file = open(file_name, 'w', encoding='utf-8')
            file.close()
        except:
            print('Файл не может быть инициализирован.')
    else:
        print('Файл не выбран, выберите файл.')


def list_split(x: str):
    """
    Функция преобразует строку базы данных в список слов базы данных
    """
    x_split = x.split('|')
    x_split.pop(0)
    x_split.pop(-1)
    return x_split


def content_output(file_name: str):
    """
    Вывод содержимого
    """
    try:
        if file_name is not None:
            max_len = list_of_maximum_lengths(file_name)
            with open(file_name, 'r', encoding='utf-8') as file:
                first_str = file.readline()
                if database_check(first_str):  # если это моя база данных
                    print('База данных:')
                    first_str_list = list_split(first_str)  # список из заголовков базы данных
                    b = formatted_output(max_len, first_str_list)
                    print(b)
                    while True:
                        string = file.readline()
                        if not string:
                            break
                        string = string.rstrip('\n')  # убираю символ перевода строк
                        string_list = list_split(string)
                        b = formatted_output(max_len, string_list)
                        print(b)
                else:
                    print('Данный файл не содержит нужной базы данных.')
        else:
            print('Файл не найден. Выберите файл.')
    except IndexError:
        print('Файл пустой. Выводить нечего.')
    except FileNotFoundError:
        print('Файла не существует.')
    except:
        print('Содержимое файла не может быть выведено.')


def add_a_note(file_name: str):
    """
    Добавление записи в файл
    """
    try:
        if file_name is not None:
            s = '| Фамилия | Имя | Отчество | Год рождения | Школа | Класс | Учебная группа |\n'
            try:
                file = open(file_name, 'r', encoding='utf-8')
                first_str = file.readline()
                file.close()
            except FileNotFoundError:
                print('Файла не существует.')
                return
            with open(file_name, 'a+', encoding='utf-8') as file:
                if not first_str:
                    file.write(s)
                if not first_str or database_check(first_str):  # если это моя база данных
                    first_str_list = list_split(s)  # список из заголовков базы данных
                    add_string = '|'
                    for i in range(len(first_str_list)):
                        while True:
                            elem_field = input(f"Введите элемент поля '{first_str_list[i].strip()}': ")
                            # убираю лишние пробелы для проверки на целое число
                            elem_field = elem_field.strip()
                            if (i == 3 or i == 5 or i == 6) and not ch.check_int(elem_field):
                                print(f"Элемент поля '{first_str_list[i].strip()}'  должен содержать в себе одно"
                                      f" целое число. Пожалуйста, введите целое число.")
                            else:
                                break
                        add_string += elem_field + '|'
                    add_string += '\n'
                    file.write(add_string)
                else:
                    print('Данный файл не содержит нужной базы данных')
        else:
            print('Файл не найден. Выберите файл.')
    except IndexError:
        print('Файл пустой.')
    except:
        print('В файл нельзя добавить запись.')


def single_field_search(file_name: str):
    """
    Поиск по одному полю
    """
    try:
        if file_name is not None:
            max_len = list_of_maximum_lengths(file_name)
            with open(file_name, 'r', encoding='utf-8') as file:
                first_str = file.readline()
                if database_check(first_str):  # если это моя база данных
                    first_str_list = list_split(first_str)  # список из заголовков базы данных
                    headlines()
                    while True:
                        number = ch.clever_input('Введите номер поля для поиска: ')
                        if number < 1 or number > len(first_str_list):
                            print(f'Неверный ввод! Номер поля - целое число от 1 до {len(first_str_list)}. '
                                  f'Пожалуйста, повторите ввод.')
                        else:
                            break
                    meaning = input('Введите значение, по которому требуется найти строку базы данных: ')
                    meaning = meaning.strip()
                    flag = True
                    while True:
                        string = file.readline()
                        if not string:
                            break
                        string_list = list_split(string)  # список значений полей базы данных
                        if string_list[number - 1].strip() == meaning:
                            b = formatted_output(max_len, string_list)
                            if flag:
                                print('Строки базы данных, удовлетворяющие условию поиска:')
                                flag = False
                            print(b)
                    if flag:
                        print('Строк, удовлетворяющих условию поиска, не нашлось.')
                else:
                    print('Файл не содержит нужной базы данных.')
        else:
            print('Файл не найден. Выберите файл.')
    except IndexError:
        print('Файл пустой. Ничего найти нельзя.')
    except FileNotFoundError:
        print('Файла не существует.')
    except Exception:
        print('Поиск по одному полю невозможен.')


def search_by_two_fields(file_name: str):
    """
    Поиск по двум полям
    """
    try:
        if file_name is not None:
            max_len = list_of_maximum_lengths(file_name)
            with open(file_name, 'r', encoding='utf-8') as file:
                first_str = file.readline()
                if database_check(first_str):  # если это моя база данных
                    first_str_list = list_split(first_str)  # список из заголовков базы данных
                    headlines()
                    while True:
                        number_1 = ch.clever_input('Введите номер 1-го поля для поиска: ')
                        if number_1 < 1 or number_1 > len(first_str_list):
                            print(f'Неверный ввод! Номер поля - целое число от 1 до {len(first_str_list)}')
                        else:
                            break
                    while True:
                        number_2 = ch.clever_input('Введите номер 2-го поля для поиска: ')
                        if number_2 < 1 or number_2 > len(first_str_list):
                            print(f'Неверный ввод! Номер поля - целое число от 1 до {len(first_str_list)}')
                        elif number_2 == number_1:
                            print('Неверный ввод! Номер 2-го поля не должен совпадать с номером 1-го поля.')
                        else:
                            break
                    meaning_1 = input('Введите значение для 1-го поля, '
                                      'по которому требуется найти строку базы данных: ')
                    meaning_2 = input('Введите значение для 2-го поля, '
                                      'по которому требуется найти строку базы данных: ')
                    meaning_1 = meaning_1.strip()
                    meaning_2 = meaning_2.strip()
                    flag = True
                    while True:
                        string = file.readline()
                        if not string:
                            break
                        string_list = list_split(string)  # список значений полей базы данных
                        if string_list[number_1 - 1].strip() == meaning_1 and \
                                string_list[number_2 - 1].strip() == meaning_2:
                            b = formatted_output(max_len, string_list)
                            if flag:
                                print('Строки базы данных, удовлетворяющие условиям поиска:')
                                flag = False
                            print(b)
                    if flag:
                        print('Строк, удовлетворяющих условиям поиска, не нашлось.')
                else:
                    print('Файл не содержит нужной базы данных.')
        else:
            print('Файл не найден. Выберите файл.')
    except IndexError:
        print('Файл пустой. Ничего найти нельзя.')
    except FileNotFoundError:
        print('Файла не существует.')
    except Exception:
        print('Поиск по одному полю невозможен.')


menu()
working_file = None

while True:
    item_numb = item_number()
    if item_numb == 1:
        working_file = name_file()
    if item_numb == 2:
        database_initialization(working_file)
    if item_numb == 3:
        content_output(working_file)
    if item_numb == 4:
        add_a_note(working_file)
    if item_numb == 5:
        single_field_search(working_file)
    if item_numb == 6:
        search_by_two_fields(working_file)
    if item_numb == 7:
        exit()
    menu()
