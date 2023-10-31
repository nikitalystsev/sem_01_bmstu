# Лысцев Н.Д. ИУ7-13Б
# Формирование матрицы из двух списков по формуле,
# нахождение среднего арифметического положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического
#
# Ввод:
# ввод 2-х списков
#
# Вывод:
# В строке по порядку выводятся матрицу A в
# виде матрицы и рядом столбцы AV и L
from math import sin

import checks as ch

while True:
    n = ch.clever_input('Введите количество элементов в обоих массивах: ')
    if n <= 0:
        print('Неверный ввод! количество элементов в обоих массивах не может быть меньше нуля или равно нулю.')
    else:
        break

d = [0] * n
f = [0] * n
for i in range(n):
    d[i] = ch.clever_input_2('Введите число - элемент массива D: ')

for i in range(n):
    f[i] = ch.clever_input_2('Введите число - элемент массива F: ')

a = [[float('{:10.5g}'.format(sin(j + k))) for j in d] for k in f]
av = []
l = []
for i in a:
    c = 0
    c1 = 0
    sum_elem = 0
    for elem in i:
        if elem > 0:
            c += 1
            sum_elem += elem
    if c != 0:
        ar_mean = sum_elem / c
        for elem in i:
            if elem < ar_mean:
                c1 += 1

        av.append(ar_mean)
        l.append(c1)
    else:
        av.append('-')
        l.append(0)

for i in range(len(a)):
    for j in range(len(a)):
        print('{:<10.7g}'.format(a[i][j]), end='')
    if av[i] == '-':
        print('{}                    {:<10.7g}         '.format(av[i], l[i]))
    else:
        print('{:<10.7g}           {:<10.7g}         '.format(av[i], l[i]))