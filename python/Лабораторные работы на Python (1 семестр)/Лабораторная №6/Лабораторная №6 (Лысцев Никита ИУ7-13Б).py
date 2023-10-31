# Лысцев Н. Д. ИУ7-13Б
# Программа, которая с помощью меню обеспечивает работу с числовыми массивами
#
# Ввод
# меню из предложенных действий
# выбор номера пункта
#
# Вывод
# результат выполнения программы


def check_int(entry):
    """
    Проверка числа на int. Возвращает True, если число целое и
    False, если число нельзя привести к целому типу данных
    """
    entry = entry.replace('_', '')
    if entry[0] == '-' or entry[0] == '+':
        entry = entry[1:]
    return entry.isdigit()


def check_float(entry):
    """
    Проверка числа на float. Возвращает True, если число вещественное и
    False, если число нельзя привести к вещественному  типу данных
    """
    if entry[0] == '-' or entry[0] == '+':
        entry = entry[1:]
    point_split = entry.split('.')
    if len(point_split) == 1:  # Нет точки
        exp_split = entry.split('e')
        if len(exp_split) == 1:  # Нет е и нет точки
            return entry.isdigit()
        elif len(exp_split) == 2:  # Есть один символ е и нет точки
            return (exp_split[0].isdigit() and (
                    exp_split[1][0] in '+-' and exp_split[1][1:].isdigit() or exp_split[1].isdigit()))

    elif len(point_split) == 2:  # Есть одна точка
        exp_split = point_split[1].split('e')
        if len(exp_split) == 1:  # Есть точка и нет е
            return point_split[0].isdigit() and exp_split[0].isdigit()
        elif len(exp_split) == 2:  # Есть точка и есть е
            return (point_split[0].isdigit() and exp_split[0].isdigit() and (
                    exp_split[1][0] in '+-' and exp_split[1][1:].isdigit() or exp_split[1].isdigit()))
    return False


def menu():
    """
    Функция выводит строку меню
    """
    print("""
    1) Проинициализировать список первыми N элементами заданного в л/р 5 ряда
    2) Очистить список и ввести его с клавиатуры
    3) Добавить элемент в произвольное место списка
    4) Удалить произвольный элемент из списка (по номеру)
    5) Очистить список
    6) Найти значение K-го экстремума в списке
    7) Найти наиболее длинную последовательность чисел, в которой все, начиная с 3-го, являются суммой
       двух предыдущих.
    8) Прекращение работы программы
    """)


def menu_item_number():
    """
    Функция просит пользователя выбрать номер пункта меню и возвращает это номер
    """
    while True:
        q = ''
        while not q:
            q = input('Введите номер пункта: ')

        if check_int(q):
            if q[0] == '-':
                print('Номер пункта не может быть отрицательным. Пожалуйста, повторите ввод.')
            elif q.count('0') == len(q):
                print('Номер пункта не может равняться нулю. Пожалуйста, повторите ввод. ')
            elif len(q) - q.count('0') > 1 or q[-1] in '09':
                print('Неверный ввод! Такого номера пункта нет. Пожалуйста, повторите ввод')
            else:
                q = int(q)
                break
        else:
            print('Пожалуйста, введите целое число')
    return q


def list_initialisation():
    """
     Функция инициализирует список первыми N элементами заданного в л/р 5 ряда и возвращает список
    """
    while True:
        N = ''
        while not N:
            N = input('Введите размер списка: ')

        if check_int(N):
            if N[0] == '-':
                print('Длина списка не может быть отрицательной. Пожалуйста, повторите ввод.')
            elif N.count('0') == len(N):
                print('Длина списка не может равняться нулю. Пожалуйста, повторите ввод. ')
            else:
                N = int(N)
                break
        else:
            print('Пожалуйста, введите целое число')

    while True:
        x = ''
        while not x:
            x = input('Введите значение аргумента: ')

        if check_float(x):
            x = float(x)
            break
        else:
            print('Пожалуйста, введите число')

    array = [0] * N
    n, m = 1, 1
    for i in range(N):
        t = 2 * ((x ** n) / m)
        array[i] = float('{:.6g}'.format(t))
        n += 2
        m += 2

    return array


def clearing_and_entering(array):
    """
    Функция очищает непустой  список и просит вользователя ввести его с клавиатуры
    Вазвращает список
    """
    if array:
        array.clear()
        print('Список очищен')
    while True:
        N = ''
        while not N:
            N = input('Введите размер списка: ')

        if check_int(N):
            if N[0] == '-':
                print('Длина списка не может быть отрицательной. Пожалуйста, повторите ввод.')
            elif N.count('0') == len(N):
                print('Длина списка не может равняться нулю. Пожалуйста, повторите ввод. ')
            else:
                N = int(N)
                break
        else:
            print('Пожалуйста, введите целое число')
    array = [0] * N
    for i in range(N):
        while True:
            h = ''
            while not h:
                h = input('Введите {}-й элемент: '.format(i + 1))

            if check_float(h):
                h = float(h)
                array[i] = h
                break
            else:
                print('Пожалуйста, введите число')

    return array


def add_item(array):
    """
    Функция, которая добавляет элемент в произвольное место списка
    Возвращает список
    """
    while True:
        n = ''
        while not n:
            n = input('Введите номер, на который будет поставлен новый элемент: ')

        if check_int(n):
            if n[0] == '-':
                print('Введенный номер не может быть отрицательным. Пожалуйста, повторите ввод.')
            elif n.count('0') == len(n):
                print('Введенный номер не может равняться нулю. Пожалуйста, повторите ввод. ')
            else:
                n = int(n)
                break
        else:
            print('Пожалуйста, введите целое число')

    if n > len(array):
        print('Веденный элемент будет добавлен в конец списка, так как введенный номер больше длины списка')

    while True:
        x = ''
        while not x:
            x = input('Введите значение нового элемента: ')

        if check_float(x):
            x = float(x)
            break
        else:
            print('Пожалуйста, введите число')

    if n > len(array):
        array.insert(n, x)
    else:
        array.insert(n - 1, x)
    return array


def remove_item(array):
    """
    Функция, которая удаляет выбранный пользователем элемент из списка (по номеру)
    Возвращает список
    """
    while True:
        n = ''
        while not n:
            n = input('Введите номер элемента, который будет удаллен: ')

        if check_int(n):
            if n[0] == '-':
                print('Номер элемента не может быть отрицательным. Пожалуйста, повторите ввод.')
            elif n.count('0') == len(n):
                print('Номер элемента не может равняться нулю. Пожалуйста, повторите ввод. ')
            else:
                n = int(n)
                break
        else:
            print('Пожалуйста, введите целое число')
    if len(array) == 0:
        print('Список пустой. Удаление невозможно')
    elif n <= len(array):
        array.pop(n - 1)
    elif n > len(array):
        print('Будет удален последний элемент списка, так как введенный номер больше, чем длина списка ')
    return array


def clear_the_list(array):
    """
    Функция, которая очищает непустой список
    Возвращает список
    """
    if array:
        array.clear()
        print('Список очищен')
    else:
        print('Список пустой')
    return array


def finding_the_Kth_extremum(array):
    """
    Функция, которая находит значение K-го экстремума в списке
    """
    while True:
        K = ''
        while not K:
            K = input('Введите номер экстремума, который требуется найти: ')

        if check_int(K):
            if K[0] == '-':
                print('Номер экстремума не может быть отрицательным. Пожалуйста, повторите ввод.')
            elif K.count('0') == len(K):
                print('Номер экстремума не может равняться нулю. Пожалуйста, повторите ввод. ')
            else:
                K = int(K)
                break
        else:
            print('Пожалуйста, введите целое число')

    c = 0
    for i in range(1, len(array) - 1):
        if ((array[i] > array[i + 1] and array[i] > array[i - 1]) or
                (array[i] < array[i + 1] and array[i] < array[i - 1])):
            c += 1
            if c == K:
                print('K-й экстремум равен: ', array[i])
                break
    if len(array) == 0:
        print('Список пустой, в нем нет экстремумов')
    elif K > c and len(array) != 0:
        print('В списке нет К-го экстремума. Экстремумов всего', c)


def similar_Fibonacci_sequence(array):
    """
    Функция, которая находит наиболее длинную последовательность чисел,
    в которой все, начиная с 3-го, являются суммой двух предыдущих
    """
    c = []
    c1 = []

    for i in range(2, len(array)):
        for j in range(i - 1, i):
            for l in range(i - 2, i - 1):
                if array[i] == array[l] + array[j]:
                    if len(c) < 2:
                        c.extend((array[l], array[j], array[i]))
                        if len(c) > len(c1):
                            c1 = c[:]

                    else:
                        c.append(array[i])
                        if len(c) > len(c1):
                            c1 = c[:]
                else:
                    c = []
    if len(c1) != 0:
        print('Наиболее длинная последовательность: ', *c1, 'Длина последовательности: ', len(c1))
    else:
        print('К сожалению, такой последовательности в списке не оказалось')


# Вызов необходимых функций для обеспечения работы со списком
menu()
q = menu_item_number()

# Создаем пустой список, который  в цикле ниже будет обрабатываться
array = []

# В цикле происходит работа со списками,
# в зависимости от номера пункта выполняются определенный действия
while True:
    # Пользователь инициализирует список первыми N элементами заданного в л/р 5 ряда
    if q == 1:
        print('Список сейчас: ', array)
        array = list_initialisation()
        print('Список после: ', array)

        menu()
        q = menu_item_number()
    # Пользоватль очищает непустой  список и просит вользователя ввести его с клавиатуры
    if q == 2:
        print('Список сейчас: ', array)
        array = clearing_and_entering(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()
    # Пользователь добавляет элемент в произвольное место списка
    if q == 3:
        print('Список сейчас: ', array)
        array = add_item(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()
    # Пользователь удаляет выбранный элемент из списка (по номеру)
    if q == 4:
        print('Список сейчас: ', array)
        array = remove_item(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()
    # Пользователь очищает непустой список
    if q == 5:
        print('Список сейчас: ', array)
        array = clear_the_list(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()
    #  Пользователь находит значение K-го экстремума в списке (если таковой существует)
    if q == 6:
        print('Список сейчас: ', array)
        finding_the_Kth_extremum(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()
    # Пользователь находит наиболее длинную последовательность чисел,
    # в которой все, начиная с 3-го, являются суммой двух предыдущих
    # (если такая последовательность существует)
    if q == 7:
        print('Список сейчас: ', array)
        similar_Fibonacci_sequence(array)
        print('Список после: ', array)

        menu()
        q = menu_item_number()
    # Пользователь прекращает работу этой программы
    if q == 8:
        exit()
