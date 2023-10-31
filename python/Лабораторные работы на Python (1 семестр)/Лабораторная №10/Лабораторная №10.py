# Лысцев Н. Д. ИУ7-13Б
# Вычисление приближенного значения интеграла методом трапеций и 3/8
#
# Ввод:
# Начало, конец отрезка, на котором будет считаться приближенное значение интеграла.
# Также введение требуемой точности для вычисления количества участков разбиения,
# максимальное количество итераций при вычислении количества участков разбиения
#
# Вывод:
# Таблица с вычисленными двумя методами интегралами,
# таблицы с абсолютной и относительной погрешностью измерений,
# определение, какой метод менее точный,
# и собственно для него вывод необходимого количества участков разбиения для вычисления интеграла с заданной точностью
import checks as ch


def data_entry():
    """
    Функция, которая просит пользователя ввести необходимые значения
    """
    a = ch.clever_input_2('Введите начало отрезка: ')
    while True:
        b = ch.clever_input_2('Введите конец отрезка: ')
        if a > b:
            print('Неверный ввод! Начало отрезка не может быть меньше конца отрезка. Пожалуйста, повторите ввод.')
        elif a == b:
            print('Неверный ввод! Начало отрезка не может совпадать с концом отрезка. Пожалуйста, повторите ввод.')
        else:
            break

    n_1 = ch.clever_input('Введите количество участков разбиений N1: ')
    n_2 = ch.clever_input('Введите количество участков разбиений N2: ')
    return a, b, n_1, n_2


def data_entry_2():
    """
    Еще одна функция, которая просит пользователя ввести необходимые значения
    """
    accuracy = ch.clever_input_2('Введите требуемую точность вычисления: ')
    max_iter = ch.clever_input('Введите максимальное количество итераций: ')
    return accuracy, max_iter


def f(x):
    """
    Интегрируемая функция
    """
    return x ** 2


def p(x):
    """
    Первообразная функции
    """
    return (x ** 3) / 3


def real_integral(a, b):
    """
    Функция, считающая действительное значение интеграла через первообразную
    """
    return p(b) - p(a)


def trapezium_method_integral(a, b, n):
    """
    Вычисление приближенного значения интеграла методом трапеций
    """
    h = (b - a) / n
    area = 0
    x = a
    func2 = f(x)
    for k in range(n):
        func = func2
        func2 = f(a + (k + 1) * h)
        area += (func + func2) / 2
    integral = h * area
    return integral


def integral_3_8_method(a, b, n):
    """
    Вычисление приближенного значения интеграла методом 3/8
    """
    if n % 3 == 0:
        h = (b - a) / n
        area = 0
        x2 = a
        func2 = f(x2)
        for k in range(n):
            func = func2
            func2 = f(a + (k + 1) * h)
            x = x2
            x2 = a + (k + 1) * h
            area += ((func + 3 * f((2 * x + x2) / 3) + 3 * f((x + 2 * x2) / 3) + func2) / 8)
        integral = h * area
        return integral
    return '-'


def absolute_error_method_trapezium(a, b, n):
    """
    Вычисление абсолютной погрешности метода трапеций
    """
    absolute_error = abs(trapezium_method_integral(a, b, n) - real_integral(a, b))
    return absolute_error


def relative_error_method_trapezium(a, b, n):
    """
    Вычисление относительной погрешности метода трапеций
    """
    relative_error = (absolute_error_method_trapezium(a, b, n) / real_integral(a, b)) * 100
    return relative_error


def absolute_error_method_3_8(a, b, n):
    """
    Вычисление абсолютной погрешности метода 3/8
    """
    if n % 3 == 0:
        absolute_error = abs(integral_3_8_method(a, b, n) - real_integral(a, b))
        return absolute_error
    return '-'


def relative_error_method_3_8(a, b, n):
    """
    Вычисление относительной погрешности метода трапеций
    """
    if n % 3 == 0:
        relative_error = (absolute_error_method_3_8(a, b, n) / real_integral(a, b)) * 100
        return relative_error
    return '-'


def table(numb1, numb2, expression1, expression2, expression3, expression4):
    """
    Функция, которая выводит таблицу
    """
    print('----------------------------------------------------------------')
    print('|                | N1 = {:<15.7g} | N2 = {:<15.7g} |'.format(numb1, numb2))
    print('----------------------------------------------------------------')
    print('| Метод трапеций |   {:^15.7g}    |   {:^15.7g}    |'.format(
        expression1, expression2))
    print('----------------------------------------------------------------')
    if expression3 == '-' and expression4 == '-':
        print('|  Метод 3/8     |           -          |           -          |')
    elif expression3 == '-':
        print('|  Метод 3/8     |           -          |   {:^15.7g}    |'.format(
            expression4))
    elif expression4 == '-':
        print('|  Метод 3/8     |   {:^15.7g}    |           -          |'.format(
            expression3))
    else:
        print('|  Метод 3/8     |   {:^15.7g}    |   {:^15.7g}    |'.format(
            expression3, expression4))
    print('----------------------------------------------------------------')


def which_method_less_accurate(error1, error2, error3, error4):
    """
    Функция, которая определяет какой метод менее точный
    """
    if error3 == '-' and error4 == '-':
        return 'Метод трапеций'
    elif error3 == '-':
        if error2 > error4:
            return 'Метод трапеций'
        elif error2 == error4:
            return 'Погрешности одинаковы, точность обоих методов равнозначна'
        else:
            return 'Метод 3/8'
    elif error4 == '-':
        if error1 > error3:
            return 'Метод трапеций'
        elif error1 == error3:
            return 'Погрешности одинаковы, точность обоих методов равнозначна'
        else:
            return 'Метод 3/8'
    else:
        ar_mean_1 = (error1 + error2) / 2
        ar_mean_2 = (error3 + error4) / 2
        if ar_mean_1 > ar_mean_2:
            return 'Метод трапеций'
        elif ar_mean_1 == ar_mean_2:
            return 'Погрешности одинаковы, точность обоих методов равнозначна'
        else:
            return 'Метод 3/8'


def calculating_number_partitions(func, a, b):
    """
    Вычисление количества разбиений для вычисления интеграла с заданной точностью для менее точного метода
    """
    n = 1
    n_ = 2
    eps, max_numb_iterations = data_entry_2()
    integral_2 = func(a, b, n)
    for i in range(max_numb_iterations):
        integral_1 = integral_2
        integral_2 = func(a, b, n_)

        if abs(integral_1 - integral_2) < eps:
            return n
        else:
            n = n_
            n_ *= 2
    print('Нужное число разбиений не вычислено за указанное количество итераций. ')


def check_none_for_accuracy(x):
    """
    Если x не None, то выводит x
    """
    if x is not None:
        print('Необходимое число разбиений для вычисления интеграла с заданной точностью: ', x)


# Получаем введенные пользователем данные
start, end, n1, n2 = data_entry()

# Вычисление интегралов
integral_1_1 = trapezium_method_integral(start, end, n1)
integral_1_2 = trapezium_method_integral(start, end, n2)

integral_2_1 = integral_3_8_method(start, end, n1)
integral_2_2 = integral_3_8_method(start, end, n2)

# Вывод таблицы со значениями вычисленных интегралов и их методами при двух разных разбиениях
print('Таблица со значениями интегралов, вычисленных методами трапеций и 3/8:')
table(n1, n2, integral_1_1, integral_1_2, integral_2_1, integral_2_2)
print('Действительное значение интеграла: {:<15.7g}'.format(p(end) - p(start)))
print()

# Вычисление абсолютной погрешности расчетов интегралов
absolute_error_1_1 = absolute_error_method_trapezium(start, end, n1)
absolute_error_1_2 = absolute_error_method_trapezium(start, end, n2)

absolute_error_2_1 = absolute_error_method_3_8(start, end, n1)
absolute_error_2_2 = absolute_error_method_3_8(start, end, n2)

# Вывод таблицы со значениями абсолютных погрешностей
print('Абсолютная погрешность:')
table(n1, n2, absolute_error_1_1, absolute_error_1_2, absolute_error_2_1, absolute_error_2_2)
print()

# Вычисление относительной погрешности
relative_error_1_1 = relative_error_method_trapezium(start, end, n1)
relative_error_1_2 = relative_error_method_trapezium(start, end, n2)

relative_error_2_1 = relative_error_method_3_8(start, end, n1)
relative_error_2_2 = relative_error_method_3_8(start, end, n2)

# Вывод таблицы со значениями относительных погрешностей
print('Относительная погрешность (в процентах):')
table(n1, n2, relative_error_1_1, relative_error_1_2, relative_error_2_1, relative_error_2_2)
print()

# В переменной хранится название наименее точного метода
least_accurate = which_method_less_accurate(absolute_error_1_1, absolute_error_1_2, absolute_error_2_1,
                                            absolute_error_2_2)

# Для наименее точного метода вычисляется количество разбиений для вычисления интеграла с заданной точностью
if least_accurate == 'Метод трапеций':
    print('Наименее точный метод: ', least_accurate)
    required_number_of_partitions = calculating_number_partitions(
        trapezium_method_integral, start,
        end)
    check_none_for_accuracy(required_number_of_partitions)
elif least_accurate == 'Метод 3/8':
    print('Наименее точный метод: ', least_accurate)
    required_number_of_partitions = calculating_number_partitions(
        integral_3_8_method, start,
        end)
    check_none_for_accuracy(required_number_of_partitions)
else:
    print('Методы равнозначны. Менее точного нет')
