# Лысцев Н.Д. ИУ7-13Б
# В заданных номерах строк матрицы определить максимальные элементы
#
# Ввод:
# ввод количества строк и столбцов матрицы d,
# а также ввод самой этой матрицы
#
# Вывод:
# матрица d, список с количеством максимальных элементов,
# список с заданными номерами строк,
# а также среднее арифметическое

import checks as ch

while True:
    n = ch.clever_input('Введите количество строк матриц d: ')
    if n <= 0:
        print('Неверный ввод! Количество строк не может быть меньше нуля или равняться нулю.')
    else:
        break

while True:
    m = ch.clever_input('Введите количество столбцов матриц d: ')
    if m <= 0:
        print('Неверный ввод! Количество столбцов не может быть меньше нуля или равняться нулю.')
    else:
        break

d = [[ch.clever_input_2('Введите {}-й элемент {}-й строки матрицы d: '.format(j + 1, i + 1)) for j in range(m)] for i in
     range(n)]
l = []
r = []

while True:
    k = ch.clever_input('Введите количество элементов в массиве l: ')
    if k <= 0:
        print('Неверный ввод! Количество элементов не может быть меньше нуля или равняться нулю.')
    else:
        break

for i in range(k):
    while True:
        number_row = ch.clever_input(
            'Введите номер строки матрицы d, для которых нужно определить максимальный элемент:')
        if number_row <= 0 or number_row > n:
            print('Неверный ввод! Номер строки - целое число от 1 до {}.'.format(n))
        else:
            break
    l.append(number_row)

length_l = len(l)
index_elem = 0
while index_elem < len(l):
    if l.count(l[index_elem]) > 1:
        del l[index_elem]
    else:
        index_elem += 1
if length_l != len(l):
    print('Произошло изменение списка c l с номерами строк, остались только уникальные номера строк, '
          'повряющиеся номера строк были заменены на один номер.')
# l = list(set(l))


for i in l:
    k = max(d[i - 1])
    r.append(k)

ar_mean = sum(r) / len(r)

print('Матрица d: ')
for i in range(n):
    for j in range(m):
        print('{:<10.7g}'.format(d[i][j]), end='')
    print()

print('Список l:', l)
print('Список r:', r)
print('Среднее арифметическое:', ar_mean)
