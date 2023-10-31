# Лысцев Н.Д. ИУ7-13Б
# Формирование новой матрицы путем перемножения 2-х старых
#
# Ввод:
# ввод 2-х матриц одинаковой размерности
#
# Вывод:
# сформированная матрица, а также список с суммой элементов ее столбцов

import checks as ch

while True:
    n = ch.clever_input('Введите количество строк матриц a и b: ')
    if n <= 0:
        print('Неверный ввод! Количество строк не может быть меньше нуля или равняться нулю.')
    else:
        break

while True:
    m = ch.clever_input('Введите количество столбцов матриц a и b: ')
    if m <= 0:
        print('Неверный ввод! Количество столбцов не может быть меньше нуля или равняться нулю.')
    else:
        break

a = [[ch.clever_input_2('Введите {}-й элемент {}-й строки матрицы a: '.format(j + 1, i + 1)) for j in range(m)] for i in
     range(n)]

print()

b = [[ch.clever_input_2('Введите {}-й элемент {}-й строки матрицы b: '.format(j + 1, i + 1)) for j in range(m)] for i in
     range(n)]

c = []

print('Матрица a: ')
for i in range(n):
    for j in range(m):
        print('{:10.7g}'.format(a[i][j]), end='')
    print()

print()

print('Матрица b: ')
for i in range(n):
    for j in range(m):
        print('{:10.7g}'.format(b[i][j]), end='')
    print()

print()

for i in range(n):
    c.append([])
    for j in range(m):
        pr = a[i][j] * b[i][j]
        c[i].append(pr)

v = []
for j in range(m):
    sum_column = 0
    for i in range(n):
        sum_column += c[i][j]
    v.append(sum_column)

print('Матрица c: ')
for i in range(n):
    for j in range(m):
        print('{:10.7g}'.format(c[i][j]), end='')
    print()

print()

print('Список с суммой каждого столбца сформированной матрицы:')
print(v)
