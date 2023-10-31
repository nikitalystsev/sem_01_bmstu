# Лысцев Н. Д. ИУ7-13Б
# Программа, которая с помощью меню обеспечиват работу со списком
#
# Ввод
# меню из предложенных действий
# выбор номера пункта
#
# Вывод
# результат выполнения программы


def check_int(x: str):
    """
    Функция, которая возвращает True, если строка - целое число. Иначе - False
    """
    x = x.replace('_', '')
    if x[0] == '-' or x[0] == '+':
        x = x[1:]
    return x.isdigit()


def menu():
    """
    Функция, которая выводит пользователю меню для работы со списком
    """
    print("""
    1) Очистить список и ввести его с клавиатуры
    2) Добавить элемент в произвольное место списка
    3) Удалить произвольный элемент из списка (по номеру)
    4) Очистить список
    5) Поиск элемента с наибольшим числом подряд идущих цифр
    6) Замена двух подряд идущих цифр на последнюю цифру их суммы
    7) Прекращение работы программы
    """)


def menu_item_number():
    """
    Функция, которая просит ввести пользователю номер пункта и возвращает его
    """
    while True:
        q = input('Введите номер пункта: ')
        if check_int(q):
            q = int(q)
            if q > 7 or q < 1:
                print('Неверный ввод! Номер пункта - целое число от 1 до 7. '
                      'Пожалуйста, повторите ввод.')
            else:
                return q
        else:
            print('Пожалуйста, введите целое число от 1 до 7.')


def clearing_and_entering(array: list):
    """
    Функция, которая очищает непустой список и просит пользователя ввести его с клавиатуры
    """
    if array:
        print('Список очищен')
        array.clear()

    else:
        print('Список и так пуст, очищать нечего')

    while True:
        N = input('Введите размер списка: ')
        if check_int(N):
            N = int(N)
            if N < 0:
                print('Неверный ввод! Размер списка не может быть отрицательным. '
                      'Пожалуйста, повторите ввод.')
            else:
                array = [0] * N
                for i in range(N):
                    array[i] = input('Введите {}-й элемент списка: '.format(i + 1))
                return array
        else:
            print('Пожалуйста, введите целое число.')


def add_item(array: list):
    """
    Функция, которая добавляет элемент в выбранное пользователем место списка
    """
    if not array:
        print('Список пустой, новый элемент будет добавлен в конец.')
        new_elem = input('Введите новый элемент: ')
        array.append(new_elem)
        return array
    else:
        while True:
            n = input('Введите номер, на который будет поставлен новый элемент: ')
            if check_int(n):
                n = int(n)
                if n <= 0:
                    print('Неверный ввод! Номер, на который будет поставлен новый элемент,'
                          ' не может быть отрицательным или равным нулю. Пожалуйста, повторите ввод.')
                elif n > len(array):
                    print('Так как введенный номер превысил длину списка, то новый элемент добавится в конец')
                    new_elem = input('Введите новый элемент: ')
                    array.append(new_elem)
                    return array
                else:
                    new_elem = input('Введите новый элемент: ')
                    array.append(new_elem)
                    for i in range(len(array) - 1, n - 1, -1):
                        array[i] = array[i - 1]
                    array[n - 1] = new_elem
                    return array
            else:
                print('Пожалуйста, введите целое число.')


def remove_item(array: list):
    """
    Функция, которая удаляет произвольный элемент списка (по номеру)
    """
    if not array:
        print('Список пустой, удалять нечего.')
        return array
    while True:
        n = input('введите номер элемента, который будет удален: ')
        if check_int(n):
            n = int(n)
            if n <= 0:
                print('Неверный ввод! Номер, который будет удален,'
                      ' не может быть отрицательным или равным нулю. Пожалуйста, повторите ввод.')
            elif n > len(array):
                print('Так как введенный номер превысил длину списка, то будет удален последний элемент')
                del array[-1]
                return array
            else:

                for i in range(n - 1, len(array) - 1):
                    array[i] = array[i + 1]
                del array[-1]
                return array
        else:
            print('Пожалуйста, введите целое число.')


def clear_the_list(array: list):
    """
    Функция, которая очищает непустой список
    """
    if array:
        print('Список очищен')
        array.clear()
        return array
    else:
        print('Список уже пуст. Очищать нечего')
        return array


def no_numbers(x: str):
    """
    Функция, которая проверяет, есть ли в строке цифры.
    Если цифр нет, то возвращает True, если же есть цифры, то возвращает False
    """
    if x:
        c = 1
        for i in range(len(x) - 1):
            if x[i] not in '0123456789' and x[i + 1] not in '0123456789':
                c += 1
        if c == len(x):
            return True
        return False
    return True


def elem_largest_number_of_consecutive_digits(array: list):
    """
    Функция, осуществляющая поиск элемента с наибольшим числом подряд идущих цифр
    """
    if not array:
        print('Список пуст. Нужного элемента не существует')
    else:
        k = float("-inf")
        m = []
        for i in range(len(array)):
            c = 1
            c1 = 1
            if no_numbers(array[i]):
                continue

            for j in range(len(array[i]) - 1):
                if array[i][j].isdigit() and array[i][j + 1].isdigit():
                    c += 1
                    c1 = max(c, c1)
                else:
                    c = 1
            if c1 > k:
                k = c1
                m = [array[i], c1]

        if not m:
            print('Ни в одном из элементов не было ряда подряд идущих цифр')
        else:
            print('Элемент с наибольшим числом подряд идущих цифр: ', m[0])
            print('Длина наибольшей последовательности подряд идущих цифр: ', m[1])


def two_consecutive_digits_on_the_last_digit_of_their_sum(array: list):
    """
    Функция, осуществляющая замену двух подряд идущих цифр на последнюю цифру их суммы
    """
    if not array:
        print('Список пуст. Ничего заменить нельзя')
        return array
    else:
        while True:
            n = input('Введите номер элемента, который будет изменён: ')
            if check_int(n):
                n = int(n)
                if n <= 0:
                    print('Неверный ввод! Номер элемента не может быть отрицательным или равным нулю. '
                          'Пожалуйста, повторите ввод.')
                elif n > len(array):
                    print('Неверный ввод! Номер элемента не может превышать длину списка. '
                          'Пожалуйста, повторите ввод. Длина списка =', len(array))
                elif no_numbers(array[n - 1]):
                    print('В выбранном элементе нет цифр, изменить нечего')
                    return array
                else:
                    array_str_n = list(array[n - 1])
                    j = 0
                    while j < (len(array_str_n) - 1):
                        if array_str_n[j].isdigit() and array_str_n[j + 1].isdigit():
                            m, k = int(array_str_n[j]), int(array_str_n[j + 1])
                            s = str(m + k)
                            w = s[-1]
                            array_str_n[j + 1] = w
                            del array_str_n[j]
                            j += 1
                        else:
                            j += 1

                    array[n - 1] = ''.join(array_str_n)
                    return array
            else:
                print('Неверный ввод! Пожалуйста, введите число.')


# Вызов меню
menu()

# Вызов функции, которая просит пользователя ввести номер пункта меню
q = menu_item_number()

# Создаем список, с которым будем работать
array = []

# В этом цикле происходит работа со списком с помощь меню
while True:
    # Если пользователь выбрал 1 пункт меню,
    # то непустой список очищается, и пользователю предлагается ввести его с клавиатуры
    if q == 1:
        print('Список сейчас: ', array)
        array = clearing_and_entering(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()

    # Если пользователь выбрал 2 пункт меню,
    # то пользователь добавляет некоторый элемент в произввольное место списка
    if q == 2:
        print('Список сейчас: ', array)
        array = add_item(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()

    # Если пользователь выбрал 3 пункт меню,
    # то пользователь удаляет тот элемент, который он выбрал
    if q == 3:
        print('Список сейчас: ', array)
        array = remove_item(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()

    # Если пользователь выбрал 4 пункт меню,
    # то непустой список очищается
    if q == 4:
        print('Список сейчас: ', array)
        array = clear_the_list(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()

    # Если пользователь выбрал 5 пункт меню,
    # то программа ищет в списке элемент с наибольшим количеством подряд идущих цифр
    if q == 5:
        print('Список сейчас: ', array)
        elem_largest_number_of_consecutive_digits(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()

    # Если пользователь выбрал 6 пункт меню,
    # то в выбранном пользователем элементе производится
    # замена двух подряд идущих цифр на последнюю цифру их суммы
    if q == 6:
        print('Список сейчас: ', array)
        array = two_consecutive_digits_on_the_last_digit_of_their_sum(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()

    # Если пользователь выбрал 7 пункт меню,
    # то работа этой программы прекращается
    if q == 7:
        exit()
