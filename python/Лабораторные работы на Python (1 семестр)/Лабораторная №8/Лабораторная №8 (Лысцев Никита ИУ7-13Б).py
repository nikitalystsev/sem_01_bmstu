# Лысцев Н. Д. ИУ7-13Б
# Программа, которая с помощью меню обеспечиват работу с целочисленной матрицей
#
# Ввод
# меню из предложенных действий
# выбор номера пункта
#
# Вывод
# результат выполнения программы


def menu():
    """
    Функция, которая выводит меню для работы с матрицей
    """
    print("""
    1) Ввести матрицу
    2) Добавить строку
        1. C помощью возможностей языка Python
        2. Алгоритмически
    3) Удалить строку
        1. C помощью возможностей языка Python
        2. Алгоритмически
    4) Добавить столбец
        1. C помощью возможностей языка Python
        2. Алгоритмически
    5) Удалить столбец
        1. C помощью возможностей языка Python
        2. Алгоритмически
    6) Наити строку, имеющую наибольшее количество четных элементов
    7) Переставить местами строки с наибольшим и наименьшим количеством
       отрицательных элементов
    8) Найти столбец, имеющий наибольшее количество чисел, являющихся степенями 2
    9) Переставить местами столбцы с максимальной и минимальной суммой
       элементов
    10)  Вывести текущую матрицу
    11) Прекращение работы программы
     """)


def check_int(x: str):
    """
    Функция, которая возвращает True, если строка - целое число. Иначе - False
    """
    if not x:
        return False
    x = x.replace('_', '')
    if x[0] == '-' or x[0] == '+':
        x = x[1:]
    return x.isdigit()


def menu_item_number():
    """
    Функция, которая возвращает введенный пользователем пункт меню
    """
    while True:
        q = input('Введите номер пункта меню: ')
        if check_int(q):
            q = int(q)
            if q > 11 or q < 1:
                print('Неверный ввод! Пожалуйста, введите челое число от 1 до 11')
            else:
                return q
        else:
            print('Неверный ввод! Пожалуйста, введите целое число от 1 до 11')


def menu_item_number_2():
    """
    Функция, которая возвращает введенный пользователем подпункт меню
    """
    while True:
        q2 = input('Введите номер подпункта меню: ')
        if check_int(q2):
            q2 = int(q2)
            if q2 > 2 or q2 < 1:
                print('Неверный ввод! Пожалуйста, введите челое число от 1 до 2')
            else:
                return q2
        else:
            print('Неверный ввод! Пожалуйста, введите целое число от 1 до 2')


def introduce_matrix(matrix: list):
    """
    Функция, позволяющая пользователю ввести матрицу
    """
    if not matrix:
        while True:
            n = input('Введите количество строк матрицы: ')
            if check_int(n):
                n = int(n)
                if n <= 0:
                    print('Неверный ввод! Количество строк матрицы не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста введите целое число')
        while True:
            m = input('Введите количество столбов матрицы: ')
            if check_int(m):
                m = int(m)
                if m <= 0:
                    print('Неверный ввод! Количество столбцов матрицы не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста введите целое число')
        for i in range(n):
            matrix.append([])
            for j in range(m):
                while True:
                    l = input('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1))
                    if check_int(l):
                        l = int(l)
                        break
                    else:
                        print('Пожалуйста, введите целое число')
                matrix[i].append(l)
        return matrix
    else:
        print('Матрица очищена')
        matrix.clear()
        while True:
            n = input('Введите количество строк матрицы: ')
            if check_int(n):
                n = int(n)
                if n <= 0:
                    print('Неверный ввод! Количество строк матрицы не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число')
        while True:
            m = input('Введите количество столбов матрицы: ')
            if check_int(m):
                m = int(m)
                if m <= 0:
                    print('Неверный ввод! Количество столбцов матрицы не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число')
        for i in range(n):
            matrix.append([])
            for j in range(m):
                while True:
                    l = input('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1))
                    if check_int(l):
                        l = int(l)
                        break
                    else:
                        print('Пожалуйста, введите целое число')
                matrix[i].append(l)
        return matrix


def add_a_line_using_python(matrix: list):
    """
    Функция, которая добавляет строку в матрице
    """
    if not matrix:
        print('Матрица пустая, строка будет добавлена в конец')
        matrix.append([])
        while True:
            n = input('Введите количество добавляемых элементов в строке: ')
            if check_int(n):
                n = int(n)
                if n < 0:
                    print('Неверный ввод! Количество добавляемых элементов в строке не может быть отрицательным. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')

        for i in range(n):
            while True:
                l = input('Введите {}-й элемент, который будет добавлен: '.format(i + 1))
                if check_int(l):
                    l = int(l)
                    break
                else:
                    print('Пожалуйста, введите целое число.')
            matrix[0].append(l)
        return matrix
    else:
        while True:
            k = input('Введите номер строки, куда будет добалена новая строка: ')
            if check_int(k):
                k = int(k)
                if k <= 0:
                    print('Неверный ввод! Номер строки не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')

        if k > len(matrix):
            print('Так как введенный пользователем номер строки превысил количество строк матрицы,'
                  ' то новая строка добавится в конец.')
            line_length = len(matrix[0])
            a = [0] * line_length
            for i in range(len(a)):
                while True:
                    l = input('Введите {}-й элемент строки: '.format(i + 1))
                    if check_int(l):
                        l = int(l)
                        break
                    else:
                        print('Пожалуйста, введите целое число.')
                a[i] = l
            matrix.append(a)
            return matrix

        else:
            line_length = len(matrix[0])
            matrix.insert(k - 1, [])
            for i in range(line_length):
                while True:
                    l = input('Введите {}-й элемент, который будет добавлен: '.format(i + 1))
                    if check_int(l):
                        l = int(l)
                        break
                    else:
                        print('Пожалуйста, введите целое число.')
                matrix[k - 1].append(l)
            return matrix


def add_a_line_algorithmically(matrix: list):
    """
    Функция, которая добавляет строку в матрице
    """
    if not matrix:
        print('Матрица пустая, строка будет добавлена в конец.')
        matrix.append([])
        while True:
            n = input('Введите количество добавляемых элементов в строке: ')
            if check_int(n):
                n = int(n)
                if n < 0:
                    print('Неверный ввод! Количество добавляемых элементов в строке не может быть отрицательным. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')

        for i in range(n):
            while True:
                l = input('Введите {}-й элемент, который будет добавлен: '.format(i + 1))
                if check_int(l):
                    l = int(l)
                    break
                else:
                    print('Пожалуйста, введите целое число.')
            matrix[0].append(l)
        return matrix
    else:
        while True:
            k = input('Введите номер строки, куда будет добалена новая строка: ')
            if check_int(k):
                k = int(k)
                if k <= 0:
                    print('Неверный ввод! Номер строки не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')

        if k > len(matrix):
            print('Так как введенный пользователем номер строки превысил количество строк матрицы,'
                  'то новая строка добавится в конец.')
            line_lenght = len(matrix[0])
            a = [0] * line_lenght
            for i in range(len(a)):
                while True:
                    l = input('Введите {}-й элемент строки: '.format(i + 1))
                    if check_int(l):
                        l = int(l)
                        break
                    else:
                        print('Пожалуйста, введите целое число.')
                a[i] = l
            matrix.append(a)
            return matrix
        else:
            line_lenght = len(matrix[0])
            a = [0] * line_lenght
            for i in range(line_lenght):
                while True:
                    l = input('Введите {}-й элемент строки: '.format(i + 1))
                    if check_int(l):
                        l = int(l)
                        break
                    else:
                        print('Пожалуйста, введите целое число.')
                a[i] = l
            matrix.append(a)
            for i in range(len(matrix) - 1, k - 1, -1):
                matrix[i] = matrix[i - 1]
            matrix[k - 1] = a
            return matrix


def delete_a_line_using_python(matrix: list):
    """
    Функция, которая удаляет строку в матрице
    """
    if not matrix:
        print('Матрица пустая, удалять нечего.')
        return matrix
    else:
        while True:
            k = input('Введите номер строки, которая будет удалена: ')
            if check_int(k):
                k = int(k)
                if k <= 0:
                    print('Неверный ввод! Номер строки не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')
        matrix.pop(k - 1)
        return matrix


def delete_a_line_algorithmically(matrix: list):
    """
    Функция, которая удаляет строку в матрице
    """
    if not matrix:
        print('Матрица пустая, удалять нечего')
        return matrix
    else:
        while True:
            k = input('Введите номер строки, которая будет удалена: ')
            if check_int(k):
                k = int(k)
                if k <= 0:
                    print('Неверный ввод! Номер строки не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')
        if k > len(matrix):
            print('Так как введенный пользователем номер строки превысил количество строк матрицы,'
                  'то будет удалена последная строка.')
            del matrix[-1]
            return matrix
        else:
            for i in range(k - 1, len(matrix) - 1):
                matrix[i] = matrix[i + 1]
            del matrix[-1]
            return matrix


def add_column_using_python(matrix: list):
    """
    Функция, которая добавляет столбец в матрице
    """
    if not matrix:
        print('Матрица пустая, столбец будет добавлен в конец.')
        while True:
            k = input('Введите количество элементов в столбце: ')
            if check_int(k):
                k = int(k)
                if k < 0:
                    print('Неверный ввод! Количество элементов в строке не может быть отрицательным. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')
        for i in range(k):
            matrix.append([])
        for j in range(k):
            while True:
                l = input('Введи {}-й элемент столбца: '.format(j + 1))
                if check_int(l):
                    l = int(l)
                    break
                else:
                    print('Пожалуйста введите целое число')
            matrix[j].append(l)
        return matrix
    else:
        while True:
            n = input('Введите номер столбца, на который будет поставлен новый столбец: ')
            if check_int(n):
                n = int(n)
                if n <= 0:
                    print('Неверный ввод! Номер столбца не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')
        if n > len(matrix[0]):
            print('Так как введенный пользователем номер столбца превысил количество стобцов матрицы,'
                  'то новый столбец добавится в конец.')
            c = 1
            for i in matrix:
                while True:
                    l = input('Введите {}-й элемент нового столбца: '.format(c))
                    if check_int(l):
                        l = int(l)
                        break
                    else:
                        print('Пожалуйста, введите целое число.')
                i.append(l)
                c += 1
            return matrix
        else:
            c = 1
            for i in matrix:
                while True:
                    l = input('Введите {}-й элемент нового столбца: '.format(c))
                    if check_int(l):
                        l = int(l)
                        break
                    else:
                        print('Пожалуйста, введите целое число.')
                i.insert(n - 1, l)
                c += 1
            return matrix


def add_column_algorithmically(matrix: list):
    """
    Функция, которая добавляет столбец в матрице
    """
    if not matrix:
        print('Матрица пустая, столбец будет добавлен в конец.')
        while True:
            k = input('Введите количество элементов в столбце: ')
            if check_int(k):
                k = int(k)
                if k < 0:
                    print('Неверный ввод! Количество элементов в столбце не может быть отрицательным. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')
        for i in range(k):
            matrix.append([])
        for j in range(k):
            while True:
                l = input('Введи {}-й элемент столбца: '.format(j + 1))
                if check_int(l):
                    l = int(l)
                    break
                else:
                    print('Пожалуйста, введите целое число.')
            matrix[j].append(l)
        return matrix
    else:
        while True:
            n = input('Введите номер столбца, на который будет поставлен новый столбец: ')
            if check_int(n):
                n = int(n)
                if n <= 0:
                    print('Неверный ввод! Номер столбца не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')
        if n > len(matrix[0]):
            print('Так как введенный пользователем номер столбца превысил количество стобцов матрицы,'
                  'то новый столбец добавится в конец.')
            c = 1
            for i in matrix:
                while True:
                    l = input('Введите {}-й элемент нового столбца: '.format(c))
                    if check_int(l):
                        l = int(l)
                        break
                    else:
                        print('Пожалуйста, введите целое число.')
                i.append(l)
                c += 1
            return matrix
        else:
            c = 1
            for i in matrix:
                a = clever_input('Введите {}-й элемент нового столбца: '.format(c))
                """
                i = [1,9,2,3,4, 5] n = 2 a = 9
                """
                i.append(a)
                for j in range(len(i) - 1, n - 1, -1):
                    i[j] = i[j - 1]
                i[n - 1] = a
            return matrix


def clever_input(s: str):
    while True:
        a = input(s)
        if check_int(a):
            a = int(a)
            break
        else:
            print('Пожалуйста, введите целое число.')
    return a


def delete_column_using_python(matrix: list):
    """
    Функция, которая удаляет стобец в матрице
    """
    if not matrix:
        print('Матрица пустая, удалять нечего.')
        return matrix
    else:
        while True:
            n = input('Введите номер столбца, который будет удален: ')
            if check_int(n):
                n = int(n)
                if n <= 0:
                    print('Неверный ввод! Номер столбца не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                else:
                    break
            else:
                print('Пожалуйста, введите целое число.')

        if n > len(matrix[0]):
            print('Так как введенный пользователем номер столбца превысил количество стобцов матрицы,'
                  'то будет удален последний столбец.')
            for i in matrix:
                del i[-1]
            return matrix
        else:
            for i in matrix:
                i.pop(n - 1)
            return matrix


def delete_column_algorithmically(matrix: list):
    """
    Функция, которая удаляет столбец в матрице
    """
    if not matrix:
        print('Матрица пустая, удалять нечего.')
        return matrix
    else:
        while True:
            n = input('Введите номер столбца, который будет удален: ')
            if check_int(n):
                n = int(n)
                if n <= 0:
                    print('Неверный ввод! Номер столбца не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                break
            else:
                print('Пожалуйста введите целое число.')
        if n > len(matrix[0]):
            print('Так как введенный пользователем номер столбца превысил количество стобцов матрицы,'
                  'то будет удален последний столбец.')
            for i in matrix:
                del i[-1]
            return matrix
        else:
            for i in matrix:
                for j in range(n - 1, len(i) - 1):
                    i[j] = i[j + 1]
                del i[-1]
            return matrix


def the_string_with_the_most_even_elements(matrix: list):
    """
    Функция, которая ищет строку с наибольшим количеством четных элементов
    """
    if not matrix:
        print('Матрица пустая, нет строки с наибольшим количеством четных элементов')
    else:
        m = float("-inf")
        for i in matrix:
            c = 0
            for j in range(len(i)):
                if i[j] % 2 == 0:
                    c += 1
            if c > m:
                m = c
                d = [i, c]

        if d[1] == 0:
            print('Строки с наибольшим количеством четным элементов в матрице нет')

        else:
            print('Строка с наибольшим количеством четных элемент: ', d[0])
            print('Количество четных элементов в строке: ', d[1])


def swap_the_lines_with_the_highest_and_lowest_count_negative_elements(matrix: list):
    """
    Функция, которая переставляет строки матрицы с с наибольшим и наименьшим количеством
    отрицательных элементов
    """
    if matrix:
        k = float("inf")
        m = float("-inf")
        for i in matrix:
            c = 0
            for j in range(len(i)):
                if abs(i[j]) != i[j]:
                    c += 1
            if c > m:
                m = c
                d = [matrix.index(i), c]
            if c < k:
                k = c
                g = [matrix.index(i), c]

        a = d[0]
        b = g[0]

        if d[1] == 0:
            print('Строк c отрицательными элементами в матрице нет')
            return matrix
        elif a == b:
            print('В матрице во всех строках количество отрицательных элементов одинаковое. '
                  'Переставлять нечего.')
            return matrix
        else:
            matrix[a], matrix[b] = matrix[b], matrix[a]
            return matrix
    else:
        print('Матрица пустая')
        return matrix


def the_largest_number_of_numbers_that_are_powers_of_2(matrix: list):
    """
    Функция, которая ищет столбец с наибольшим количество чисел, являющихся степенями 2
    """
    if not matrix:
        print('Матрица пустая')
    else:
        m = float("-inf")
        for j in range(len(matrix[0])):
            c = 0
            for i in range(len(matrix)):
                b = int(matrix[i][j])
                if bin(b).count('1') == 1 and b > 0:
                    c += 1
            if c > m:
                m = c
                d = [j, c]

        a = d[0]

        if d[1] == 0:
            print('Столбца с наибольшим количеством чисел, являющихся степенью числа 2 в матрице нет')
        else:
            print('Столбец с наибольшим количеством чисел, являющихся степенью числа 2: ')
            for i in matrix:
                print(i[a])
            print('Количество чисел, являющихся степенью 2: ', d[1])


def swap_the_columns_with_the_maximum_and_minimum_sum_elements(matrix: list):
    """
    Функция, которая переставляет местами столбцы с максимальной и минимальной суммой
    элементов
    """
    if not matrix:
        print('Матрица пустая')
        return matrix
    else:
        k = float("inf")
        m = float("-inf")
        for j in range(len(matrix[0])):
            s = 0
            for i in range(len(matrix)):
                s += matrix[i][j]
            if s > m:
                m = s
                d = [j, s]
            if s < k:
                k = s
                g = [j, s]

        a = d[0]
        b = g[0]
        if d[1] == g[1]:
            print('Все столбцы матрицы имеют одинаковую сумму элементов. Переставлять нечего.')
            return matrix
        for i in matrix:
            i[a], i[b] = i[b], i[a]
        return matrix


# Создание пустой матрицы
matrix = []

# Вызов меню
menu()

# Вызов функции, которая просит пользователя ввести номер пункта меню
q = menu_item_number()
while True:

    # Пользователь вводит матрицу
    if q == 1:
        matrix = introduce_matrix(matrix)

        menu()
        q = menu_item_number()

    # Пользователь добавляет строку
    if q == 2:
        q2 = menu_item_number_2()
        if q2 == 1:
            matrix = add_a_line_using_python(matrix)

            menu()
            q = menu_item_number()
        elif q2 == 2:
            matrix = add_a_line_algorithmically(matrix)

            menu()
            q = menu_item_number()

    # Пользователь удаляет строку
    if q == 3:
        q2 = menu_item_number_2()
        if q2 == 1:
            matrix = delete_a_line_using_python(matrix)

            menu()
            q = menu_item_number()
        else:
            matrix = delete_a_line_algorithmically(matrix)

            menu()
            q = menu_item_number()

    # Пользователь добавляет столбец
    if q == 4:
        q2 = menu_item_number_2()
        if q2 == 1:
            matrix = add_column_using_python(matrix)

            menu()
            q = menu_item_number()

        if q2 == 2:
            matrix = add_column_algorithmically(matrix)

            menu()
            q = menu_item_number()

    # Пользователь удаляет столбец
    if q == 5:
        q2 = menu_item_number_2()
        if q2 == 1:
            matrix = delete_column_using_python(matrix)

            menu()
            q = menu_item_number()
        if q2 == 2:
            matrix = delete_column_algorithmically(matrix)

            menu()
            q = menu_item_number()

    # Ищется строка с наибольшим количеством четных элементов
    if q == 6:
        the_string_with_the_most_even_elements(matrix)

        menu()
        q = menu_item_number()

    # Переставляются местами строки с наибольшим и наименьшим количеством
    # отрицательных элементов
    if q == 7:
        matrix = swap_the_lines_with_the_highest_and_lowest_count_negative_elements(matrix)

        menu()
        q = menu_item_number()

    # Ищется столбец с наибольшим количество чисел, являющихся степенями 2
    if q == 8:
        the_largest_number_of_numbers_that_are_powers_of_2(matrix)

        menu()
        q = menu_item_number()

    # Переставляются местами столбцы с максимальной и минимальной суммой
    # элементов
    if q == 9:
        matrix = swap_the_columns_with_the_maximum_and_minimum_sum_elements(matrix)

        menu()
        q = menu_item_number()

    # Выводится текущая матрица
    if q == 10:
        if not matrix:
            print('Матрица сейчас: ')
            print(matrix)
        else:
            print('Матрица сейчас: ')
            for i in matrix:
                print(i)

        q = menu_item_number()

    # Прекращение работы программы
    if q == 11:
        exit()
