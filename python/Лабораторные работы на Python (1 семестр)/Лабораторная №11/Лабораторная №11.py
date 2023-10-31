# Лысцев Н. Д. ИУ7-13Б
# Программа, которая с помощью меню обеспечивает работу с текстом
#
# Ввод
# меню из предложенных действий
# выбор номера пункта
#
# Вывод
# результат выполнения программы

import checks as ch

fragment = [
    'Россия',
    'И действительно действительно, он пробежал один только несколько ',
    'шагов. Тронулся один, другой солдат, и весь батальон с криком «ура!» побежал вперед и ',
    'обогнал его. Унтер-офицер батальона, подбежав, взял колебавшееся от тяжести в руках князя Андрея ',
    'знамя, но тотчас же2*3/6 был убит. Князь Андрей опять схватил знамя ',
    'и, волоча его за древко, бежал с батальоном. Впереди ',
    'себя он видел наших артиллеристов, из которых одни дрались, другие бросали пушки и бежали к нему ',
    'навстречу; он видел и ',
    'французских пехотных солдат, которые хватали артиллерийских лошадей и поворачивали пушки. Князь ',
    'Андрей с батальоном уже был ',
    'в двадцати шагах от орудий. Он слышал над собою не перестававший свист пуль, и ',
    '15 / 3      12 /0 беспрестанно ',
    'справа и слева от него ',
    'охали и падали солдаты. Но он не 12 / 6 смотрел на них; он вглядывался только в то, что происходило впереди ',
    'его — на батарее. Он ясно видел уже одну фигуру ',
    'рыжего артиллериста с сбитым набок кивером, тянущего с одной стороны банник, тогда ',
    'как французский солдат тянул банник к себе за другую сторону. Князь Андрей ',
    'видел уже ясно растерянное и вместе озлобленное выражение лиц этих двух людей,',
    'видимо, не понимавших ',
    'действительно того, что они делали.'
]
param = None


def menu():
    """
    Функция выводит меню
    """
    print("""
    1. Выровнять текст по левому краю
    2. Выровнять текст по правому краю
    3. Выровнять текст по ширине
    4. Удаление всех вхождений заданного слова
    5. Замена одного слова другим во всём тексте
    6. Вычисление арифметических выражений умножения и деления в тексте
    7. Отсортировать слова в лексикографическом порядке в самом длинном по количеству символов предложении
    8. Выход из программы
    """)


def menu_item():
    """
    Функция, которая возвращает номер пункта меню
    """
    while True:
        numb = ch.clever_input('Введите номер пункта меню: ')
        if numb < 1 or numb > 8:
            print('Неверный ввод! Номер пункта - целое число от 1 до 8. Пожалуйста, повторите ввод.')
        else:
            break
    return numb


def transformations(text):
    """
    Функция убирает лишние проблемы и выравнивает текст по левому краю
    """
    global param
    for i in range(len(text)):
        a = text[i].split()
        text[i] = ' '.join(a)
    param = 1
    return text


def right_alignment(text):
    """
    Функция выравнивает текст по правому краю
    """
    global param
    max_length = 0
    for i in text:
        if len(i) > max_length:
            max_length = len(i)

    text = transformations(text)

    for i in range(len(text)):
        delta = max_length - len(text[i])
        text[i] = ' ' * delta + text[i]
    param = 2
    return text


def width_alignment(text):
    """
    Выравнивание по ширине
    """
    global param
    max_length = 0
    for i in text:
        if len(i) > max_length:
            max_length = len(i)

    text = transformations(text)

    for i in range(len(text)):
        count_whitespace = 0
        a = text[i].split()
        text[i] = ' '.join(a)

        for elem in range(len(text[i])):
            if text[i][elem] == ' ':
                count_whitespace += 1
        if count_whitespace != 0:
            delta = max_length - len(text[i])
            number_spaces_added = delta // count_whitespace
            index_symbol = len(text[i]) - 1
            while index_symbol > -1:
                if text[i][index_symbol] == ' ':
                    text[i] = text[i][:index_symbol] + ' ' * number_spaces_added + text[i][index_symbol:]
                    count_whitespace -= 1
                    delta = max_length - len(text[i])
                    if count_whitespace != 0:
                        number_spaces_added = delta // count_whitespace
                elif text[i][index_symbol] == ' ' and text[i][:index_symbol].count(' ') == 0:
                    text[i] = text[i][:index_symbol] + ' ' * delta + text[i][index_symbol:]
                index_symbol -= 1
    param = 3
    return text


def last_alignment():
    """
    Функция, которая сохраняет последнее использованное пользователем выравнивание
    """
    if param == 1:
        return transformations
    elif param == 2:
        return right_alignment
    elif param == 3:
        return width_alignment


def delete_word(text):
    """
    Функция удаляет все вхождения введенного пользователем слова во всем тексте
    """
    a = ';:,.'
    global param
    flag = False
    while True:
        word = input('Введите слово, которое будет удалено: ')
        for i in range(len(text)):
            text_split = text[i].split()
            for j in range(len(text_split)):
                if text_split[j][-1] in a:
                    if word == text_split[j][:len(text_split[j]) - 1]:
                        flag = True
                        break
                else:
                    if word == text_split[j]:
                        flag = True
                        break
        if not flag:
            print('Слова, которое вы хотите удалить, либо нет в тексте, '
                  'либо является частью другого слова. Пожалуйста, повторите ввод.')
        elif len(word) == 0 or word.count(' ') == len(word):
            print('Неверный ввод! Символ пробела не считается словом. Пожалуйста, повторите ввод!')
        else:
            break

    for i in range(len(text)):
        words = text[i].split()
        for j in range(len(words)):

            if words[j][-1] in a:
                if word == words[j][:len(words[j]) - 1]:
                    words[j] = words[j].split(word)
                    words[j] = ''.join(words[j])

            else:
                if word == words[j]:
                    words[j] = words[j].split(word)
                    words[j] = ''.join(words[j])

        text[i] = ' '.join(words)
    if param is not None:
        b = last_alignment()
        text = b(text)
    return text


def replace_word(text):
    """
    Функция заменяет одно слово другим во всём тексте
    """
    a = ';:,.'
    global param
    flag = False
    while True:
        replaced_word = input('Введите заменяемое слово: ')
        for i in range(len(text)):
            text_split = text[i].split()
            for j in range(len(text_split)):
                if text_split[j][-1] in a:
                    if replaced_word == text_split[j][:len(text_split[j]) - 1]:
                        flag = True
                        break
                else:
                    if replaced_word == text_split[j]:
                        flag = True
                        break
        if not flag:
            print('Заменяемого слова нет в тексте. Пожалуйста, повторите ввод.')
        elif len(replaced_word) == 0 or replaced_word.count(' ') == len(replaced_word):
            print('Неверный ввод! Введенное выражение не считается словом. Пожалуйста, повторите ввод.')
        else:
            break

    while True:
        new_word = input('Введите новое слово: ')
        if len(new_word) == 0 or new_word.count(' ') == len(new_word):
            print('Неверный ввод! Введенное выражение не считается словом. Пожалуйста, повторите ввод.')
        else:
            break
    for i in range(len(text)):
        words = text[i].split()
        for j in range(len(words)):
            if words[j][-1] in a:
                if replaced_word == words[j][:len(words[j]) - 1]:
                    words[j] = words[j].split(replaced_word)
                    words[j] = new_word.join(words[j])

            else:
                if replaced_word == words[j]:
                    words[j] = words[j].split(replaced_word)
                    words[j] = new_word.join(words[j])

        text[i] = ' '.join(words)
    if param is not None:
        b = last_alignment()
        text = b(text)
    return text


def multiplication_and_division(text):
    """
    Вычисляет значения умножения и деления в тексте
    """
    global param
    d = '0123456789.'
    symbol = '0123456789 .'
    for w in range(len(text)):
        i = 0
        while i < (len(text[w])):
            if text[w][i] == '*' or text[w][i] == '/':
                arithmetic_sign = text[w][i]
                str_1 = ''
                str_2 = ''
                j = i - 1
                k = i + 1
                while ch.check_int(text[w][j]) or text[w][j] in symbol:
                    if text[w][j] in symbol or ch.check_int(text[w][j]):
                        if ch.check_int(text[w][j]) and text[w][j - 1] not in d:
                            str_1 += text[w][j]
                            break
                        else:
                            str_1 += text[w][j]
                            j -= 1
                    else:
                        break
                while ch.check_int(text[w][k]) or text[w][k] in symbol:
                    if text[w][k] in symbol or ch.check_int(text[w][k]):
                        if ch.check_int(text[w][k]) and text[w][k + 1] not in d:
                            str_2 += text[w][k]
                            break
                        else:
                            str_2 += text[w][k]
                            k += 1
                    else:
                        break
                str_1 = str_1[::-1]
                str_1 = str_1.replace(' ', '')
                str_2 = str_2.replace(' ', '')
                if arithmetic_sign == '*':
                    if ch.check_int(str_1) and ch.check_int(str_2):
                        result = int(str_1) * int(str_2)
                        result_str = str(result)
                        text[w] = text[w][:j] + result_str + text[w][k + 1:]
                        i = j
                else:
                    if ch.check_int(str_1) and ch.check_int(str_2):
                        if int(str_2) != 0:
                            result = int(str_1) / int(str_2)
                            result_str = '{:g}'.format(result)
                            text[w] = text[w][:j] + result_str + text[w][k + 1:]
                            i = j
            i += 1
    if param is not None:
        b = last_alignment()
        text = b(text)
    return text


def sort_alphabetically(text):
    """
    Функция, которая сортирует слова в лексикографическом
    порядке в самом длинном по количеству символов предложении
    """
    text = transformations(text)
    for i in range(len(text)):
        text[i] = ' ' + text[i]
    str_text = ''.join(text)
    split_point = str_text.split('.')

    max_length = 0
    max_i = 0
    for i in range(len(split_point)):
        if len(split_point[i]) > max_length:
            max_length = len(split_point[i])
            max_i = i

    offer_max = split_point[max_i].split()
    e = ''
    for i in sorted(offer_max, key=str.lower):
        e += i + ' '
    e += '.'
    print('Предложение с отсортированными по алфавиту словами:')
    print(e)


def works(func, text):
    """
    Функция для вывода результата работы выбранных пользователем пунктов
    """
    print('Текущий текст:')
    for i in text:
        print(i)

    text_ = func(text)

    print('Текст после изменений:')
    for i in text_:
        print(i)
    menu()
    return text_


# Цикл, который обеспечивает работу пользователю с текстом
menu()
while True:
    q = menu_item()
    if q == 1:
        fragment = works(transformations, fragment)
    if q == 2:
        fragment = works(right_alignment, fragment)
    if q == 3:
        fragment = works(width_alignment, fragment)
    if q == 4:
        fragment = works(delete_word, fragment)
    if q == 5:
        fragment = works(replace_word, fragment)
    if q == 6:
        fragment = works(multiplication_and_division, fragment)
    if q == 7:
        sort_alphabetically(fragment)
    if q == 8:
        exit()
