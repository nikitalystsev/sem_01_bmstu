# Лысцев Н. Д. ИУ7-13Б
# Программа, которая с помощью меню обеспечивает работу с базой данных в бинарном файле
#
# Ввод
# меню из предложенных действий
# выбор номера пункта
#
# Вывод
# результат выполнения программы
import checks as ch
import struct

string_format = '>30s30s30si'
string_line = struct.calcsize(string_format)


def menu():
    """
    Вывод меню
    """
    print("""
    1. Выбрать файл для работы
    2. Инициализировать базу данных
    3. Вывести содержимое базы данных
    4. Добавить запись в базу данных
    5. Удалить запись из базы данных (по номеру)
    6. Поиск по одному полю
    7. Поиск по двум полям
    0. Выход из программы
     """)


def headlines():
    """
    Вывод заголовков базы данных
    """
    print(
        '1. Фамилия\n'
        '2. Имя\n'
        '3. Отчество\n'
        '4. Класс\n'
    )


def item_number():
    """
    Возвращает номер пункта
    """
    while True:
        numb = ch.clever_input('Введите номер пункта меню: ')
        if numb < 0 or numb > 7:
            print('Неверный ввод! Номер пункта - целое число от 1 до 6. Пожалуйста, повторите ввод.')
        else:
            break
    return numb


def name_file():
    """
    Возвращает имя файла, введенное пользователем
    """
    file_name = input('Введите имя файла или полный путь к файлу: ')
    return file_name


def database_check(file_name: str):
    """
    Проверка на то, что база данных моя
    """
    with open(file_name, 'rb') as file:
        file.seek(0, 2)
        end = file.tell()
        if end % string_line != 0:
            print('Файл не содержит нужной базы данных.')
            return False
    return True


def database_initialization(file_name: str):
    """
    Инициализация базы данных
    """
    if file_name is not None:
        try:
            file = open(file_name, 'wb')
            file.close()
        except:
            print('Файл не может быть инициализирован.')
    else:
        print('Файл не выбран, выберите файл.')


def content_output(file_name: str):
    """
    Вывод содержимого
    """
    try:
        if file_name is not None:
            with open(file_name, 'rb') as file:
                file.seek(0, 2)
                end = file.tell()
                file.seek(0)
                if not database_check(file_name):
                    return
                if end == 0:
                    print('Файл пустой. Ничего вывести нельзя.')
                    return
                count_strings = end // string_line
                print('База данных:')
                print('|  ' + 'Фамилия' + ' ' * (15 - len('Фамилия')) + '|' +
                      '   ' + 'Имя' + ' ' * (15 - len('Имя')) + '|' +
                      '   ' + 'Отчество' + ' ' * (15 - len('Отчество')) + '|' +
                      '   ' + 'Класс' + ' ' * (15 - len('Класс')) + '|'
                      )
                for i in range(count_strings):
                    string = file.read(string_line)

                    string_2 = struct.unpack(string_format, string)

                    field_1 = string_2[0].decode('utf-8').replace('\x00', '')
                    field_2 = string_2[1].decode('utf-8').replace('\x00', '')
                    field_3 = string_2[2].decode('utf-8').replace('\x00', '')

                    print('|  ' + field_1 + ' ' * (15 - len(field_1)) + '|' +
                          '   ' + field_2 + ' ' * (15 - len(field_2)) + '|' +
                          '   ' + field_3 + ' ' * (15 - len(field_3)) + '|  {:^15.7g} |'.format(int(string_2[3])))
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
            s = ' Фамилия  Имя  Отчество  Класс '
            first_str_list = s.split()
            try:
                file = open(file_name, 'rb')
                file.close()
            except FileNotFoundError:
                print('Файла не существует.')
                return
            with open(file_name, 'ab+') as file:
                if not database_check(file_name):
                    return
                array_field = []
                for i in range(len(first_str_list)):
                    while True:
                        elem_field = input(f"Введите элемент поля '{first_str_list[i].strip()}': ")
                        # убираю лишние пробелы для проверки на целое число
                        elem_field = elem_field.strip()
                        if len(elem_field) > 15:
                            print(f"Неверный ввод! Длина введенного значения поля '{first_str_list[i].strip()}' "
                                  f"не должна превышать 15 символов. "
                                  f"Пожалуйста, повторите ввод. ")
                        elif i == 3 and not ch.check_int(elem_field):
                            print(f"Элемент поля '{first_str_list[i].strip()}' содержит в себе одно"
                                  f" целочисленное значение. Пожалуйста, введите целое число.")
                        else:
                            break
                    array_field.append(elem_field)
                pack_string = struct.pack(string_format, array_field[0].encode('utf-8'),
                                          array_field[1].encode('utf-8'), array_field[2].encode('utf-8'),
                                          int(array_field[3]))
                file.write(pack_string)

        else:
            print('Файл не найден. Выберите файл.')
    except:
        print('В файл нельзя добавить запись.')


def delete_entry(file_name: str):
    """
    Удаляет запись по номеру
    """
    try:
        if file_name is not None:
            try:
                file = open(file_name, 'rb')
                file.seek(0, 2)
                end = file.tell()
                file.seek(0)
                file.close()
            except FileNotFoundError:
                print('Файла не существует.')
                return
            with open(file_name, 'rb+') as file:
                if not database_check(file_name):
                    return
                if end == 0:
                    print('Файл пустой. Ничего удалить нельзя.')
                    return
                count_strings = end // string_line
                while True:
                    number_string = ch.clever_input('Введите номер строки, которую хотите удалить: ')
                    if number_string <= 0 or number_string > count_strings:
                        print(f'Неверный ввод! Номер удаляемой строки - целое число от 1 до {count_strings}')
                    else:
                        break
                number_string_new = number_string - 1  # так как нумерация всегда начинается с нуля
                for i in range(number_string_new, count_strings):
                    # перемещаем файловый указатель в конец той строки, которую хотим удалить
                    file.seek((i + 1) * string_line)
                    # считываем следующую строку
                    next_string = file.read(string_line)
                    # перемещаем файловый указатель в начало той строки, которую хотим удалить
                    file.seek(i * string_line)
                    # записываем в файл следующую строку перед той строкой, что хотим удалить
                    file.write(next_string)
                # в конце с помощью метода trancate обрезаем файл с конца то текущей позиции файлового указателя
                file.truncate()

    except:
        print('Удалить запись невозможно.')


def single_field_search(file_name: str):
    """
    Поиск по одному полю
    """
    try:
        if file_name is not None:
            s = ' Фамилия  Имя  Отчество  Класс'
            first_str_list = s.split()
            with open(file_name, 'rb') as file:
                file.seek(0, 2)
                end = file.tell()
                file.seek(0)
                if not database_check(file_name):
                    return
                if end == 0:
                    print('Файл пустой.')
                    return
                count_strings = end // string_line
                headlines()
                while True:
                    number = ch.clever_input('Введите номер поля для поиска: ')
                    if number < 1 or number > len(first_str_list):
                        print(f'Неверный ввод! Номер поля - целое число от 1 до {len(first_str_list)}')
                    else:
                        break
                meaning = input('Введите значение, '
                                'по которому требуется найти строку базы данных: ')
                meaning = meaning.strip()
                flag = True
                for i in range(count_strings):
                    array_string = []
                    string = file.read(string_line)
                    string_2 = struct.unpack(string_format, string)

                    field_1 = string_2[0].decode('utf-8').replace('\x00', '')
                    field_2 = string_2[1].decode('utf-8').replace('\x00', '')
                    field_3 = string_2[2].decode('utf-8').replace('\x00', '')
                    field_4 = string_2[3]

                    array_string += [field_1, field_2, field_3, str(field_4)]

                    if array_string[number - 1] == meaning:
                        if flag:
                            print('Строк базы данных, удовлетворяющих условию поиска:')
                            flag = False
                        print('|  ' + field_1 + ' ' * (15 - len(field_1)) + '|' +
                              '   ' + field_2 + ' ' * (15 - len(field_2)) + '|' +
                              '   ' + field_3 + ' ' * (15 - len(field_3)) + '|  {:^15.7g} |'.format(int(string_2[3])))
                if flag:
                    print('Строк, удовлетворяющих условию поиска, не нашлось.')
        else:
            print('Файл не найден. Выберите файл.')

    except IndexError:
        print('Файл пустой. Ничего найти нельзя.')
    except FileNotFoundError:
        print('Файла не существует.')
    except:
        print('Поиск по одному полю невозможен.')


def search_by_two_fields(file_name: str):
    """
    Поиск по двум полям
    """
    try:
        if file_name is not None:
            s = ' Фамилия  Имя  Отчество  Класс'
            first_str_list = s.split()
            with open(file_name, 'rb') as file:
                file.seek(0, 2)
                end = file.tell()
                file.seek(0)
                if not database_check(file_name):
                    return
                if end == 0:
                    print('Файл пустой.')
                    return
                count_strings = end // string_line
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
                        print('Неверный ввод! Номер 2-го поля не может быть равен номеру 1-го поля. '
                              'Пожалуйста, повторите ввод.')
                    else:
                        break
                meaning_1 = input('Введите значение для 1-го поля, '
                                  'по которому требуется найти строку базы данных: ')
                meaning_2 = input('Введите значение для 2-го поля, '
                                  'по которому требуется найти строку базы данных: ')
                meaning_1 = meaning_1.strip()
                meaning_2 = meaning_2.strip()
                flag = True
                for i in range(count_strings):
                    array_string = []
                    string = file.read(string_line)
                    string_2 = struct.unpack(string_format, string)

                    field_1 = string_2[0].decode('utf-8').replace('\x00', '')
                    field_2 = string_2[1].decode('utf-8').replace('\x00', '')
                    field_3 = string_2[2].decode('utf-8').replace('\x00', '')
                    field_4 = string_2[3]

                    array_string += [field_1, field_2, field_3, str(field_4)]
                    if array_string[number_1 - 1] == meaning_1 and array_string[number_2 - 1] == meaning_2:
                        if flag:
                            print('Строки базы данных, удовлетворяющие условиям поиска:')
                            flag = False
                        print('|  ' + field_1 + ' ' * (15 - len(field_1)) + '|' +
                              '   ' + field_2 + ' ' * (15 - len(field_2)) + '|' +
                              '   ' + field_3 + ' ' * (15 - len(field_3)) + '|  {:^15.7g} |'.format(
                            int(string_2[3])))
                if flag:
                    print('Строк, удовлетворяющих условиям поиска, не нашлось.')
        else:
            print('Файл не найден. Выберите файл.')

    except IndexError:
        print('Файл пустой. Ничего найти нельзя.')
    except FileNotFoundError:
        print('Файла не существует.')
    except:
        print('Поиск по двум полям невозможен.')


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
        delete_entry(working_file)
    if item_numb == 6:
        single_field_search(working_file)
    if item_numb == 7:
        search_by_two_fields(working_file)
    if item_numb == 0:
        exit()
    menu()
