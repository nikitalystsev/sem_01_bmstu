# Лысцев Н. Д. ИУ7-13Б
# Программа, которая демонстрирует работу сортировки методом Шелла
#
# Ввод
# Количества - размерности списков
#
# Вывод
# Таблица со значениями времени, потраченных программой
# на сортировку трех видов списков при различных размерностях

import checks as ch
from random import randint
import timeit


def check_dimension(number_array: str):
    """
    Проверка корректности введенной размерности списка
    """
    while True:
        n = ch.clever_input(f'Введите размерность {number_array}-го списка: ')
        if n < 0:
            print('Неверный ввод! Размерность списка не может быть меньше нуля.'
                  ' Пожалуйста, повторите ввод.')
        else:
            break
    return n


def sort_array():
    """
    Функция сортирует введенный пользователем список методом Шелла
    """
    n = check_dimension('пользовательского')
    array = [0] * n
    for i in range(n):
        array[i] = ch.clever_input(
            'Введите целое число - {}-й элемент списка: '.format(i + 1))
    print('Введенный список:', array)
    array = shell_sort(array)
    print('Отсортированный список:', array)


def shell_sort(data: list[int]):
    """
    Сортировка методом Шелла
    """
    last_index = len(data) - 1
    step = len(data) // 2  # шаг
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data


def random_array(n: int):
    """
    Создает список случайных целых чисел длины n
    """
    random_list = [randint(-1000, 1000) for _ in range(n)]
    return random_list


def sorted_array(n: int):
    """
    Возвращает отсортированный список от 0 до числа n
    """
    sorted_list = [i for i in range(n)]
    return sorted_list


def sorted_reverse(n: int):
    """
    Возвращает отсортированный в обратном порядке список от 0 до числа n
    """
    sorted_reverse_list = [i for i in range(n, 0, -1)]
    return sorted_reverse_list


def input_of_dimensions():
    """
    Возвращает 3 размерности списков
    """
    number_1 = check_dimension('1')
    number_2 = check_dimension('2')
    number_3 = check_dimension('3')
    return number_1, number_2, number_3


def table(dimension1, dimension2, dimension3, number1, number2, number3,
          number4, number5, number6, number7, number8, number9):
    """
    Функция, которая выводит таблицу
    """
    print('---------------------------------------------------------------------------------------------------------')
    print('|                                  | N1 = {:<15.7g} | N2 = {:<15.7g} | N2 = {:<15.7g} |'.format(dimension1,
                                                                                                           dimension2,
                                                                                                           dimension3))
    print('---------------------------------------------------------------------------------------------------------')
    print('| Упорядоченный список             |   {:^15.7g}    |   {:^15.7g}    |   {:^15.7g}    |'.format(number1,
                                                                                                           number2,
                                                                                                           number3))
    print('---------------------------------------------------------------------------------------------------------')
    print('| Случайный список                 |   {:^15.7g}    |   {:^15.7g}    |   {:^15.7g}    |'.format(number4,
                                                                                                           number5,
                                                                                                           number6))
    print('---------------------------------------------------------------------------------------------------------')
    print('| Упорядоченный в обратном порядка |   {:^15.7g}    |   {:^15.7g}    |   {:^15.7g}    |'.format(number7,
                                                                                                           number8,
                                                                                                           number9))
    print('---------------------------------------------------------------------------------------------------------')


sort_array()

n1, n2, n3 = input_of_dimensions()

list1_sorted = sorted_array(n1)
list1_reverse_sorted = sorted_reverse(n1)
list1_random = random_array(n1)

list2_sorted = sorted_array(n2)
list2_reverse_sorted = sorted_reverse(n2)
list2_random = random_array(n2)

list3_sorted = sorted_array(n3)
list3_reverse_sorted = sorted_reverse(n3)
list3_random = random_array(n3)

information_for_first_dimension_1 = [timeit.timeit('shell_sort(list1_sorted)', number=1, globals=globals()),
                                     timeit.timeit(
                                         'shell_sort(list1_reverse_sorted)', number=1, globals=globals()),
                                     timeit.timeit('shell_sort(list1_random)', number=1, globals=globals())]

information_for_second_dimension_1 = [timeit.timeit('shell_sort(list2_sorted)', number=1, globals=globals()),
                                      timeit.timeit(
                                          'shell_sort(list2_reverse_sorted)', number=1, globals=globals()),
                                      timeit.timeit('shell_sort(list2_random)', number=1, globals=globals())]

information_for_third_dimension_1 = [timeit.timeit('shell_sort(list3_sorted)', number=1, globals=globals()),
                                     timeit.timeit(
                                         'shell_sort(list3_reverse_sorted)', number=1, globals=globals()),
                                     timeit.timeit('shell_sort(list3_random)', number=1, globals=globals())]

table(n1, n2, n3, information_for_first_dimension_1[0], information_for_second_dimension_1[0],
      information_for_third_dimension_1[0], information_for_first_dimension_1[1], information_for_second_dimension_1[1],
      information_for_third_dimension_1[1], information_for_first_dimension_1[2], information_for_second_dimension_1[2],
      information_for_third_dimension_1[2])
