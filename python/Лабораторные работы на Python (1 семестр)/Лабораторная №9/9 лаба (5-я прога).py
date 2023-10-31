# Лысцев Н.Д. ИУ7-13Б
# Подсчитать в каждой строке матрицы d количество элементов, превышающих
# суммы элементов соответствующих строк матрицы z. Разместить эти
# количества в массиве g, умножить матрицу d на максимальный элемент
# массива g
#
# Ввод:
# ввод количества строк и столбцов матриц d и z,
# а также ввод самих этих матриц
#
# Вывод:
# матрица d до и после изменения, список g
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

while True:
    l = ch.clever_input('Введите количество строк матриц z: ')
    if n <= 0:
        print('Неверный ввод! Количество строк не может быть меньше нуля или равняться нулю.')
    else:

        break

while True:
    k = ch.clever_input('Введите количество столбцов матриц z: ')
    if m <= 0:
        print('Неверный ввод! Количество столбцов не может быть меньше нуля или равняться нулю.')
    else:
        break

d = [[ch.clever_input_2('Введите {}-й элемент {}-й строки матрицы d: '.format(j + 1, i + 1)) for j in range(m)] for i in
     range(n)]
z = [[ch.clever_input_2('Введите {}-й элемент {}-й строки матрицы z: '.format(j + 1, i + 1)) for j in range(k)] for i in
     range(l)]

print('Матрица d сначала:')
for i in range(n):
    for j in range(m):
        print('{:10.7g}'.format(d[i][j]), end='')
    print()

print('Матрица z сначала:')
for i in range(l):
    for j in range(k):
        print('{:10.7g}'.format(z[i][j]), end='')
    print()

g = []

if n > l:
    w = l
else:
    w = n

for i in range(w):
    count = 0
    sum_z = sum(z[i])
    for j in range(m):
        if d[i][j] > sum_z:
            count += 1
    g.append(count)

print('Список g: ', g)
max_g = max(g)
for i in range(n):
    for j in range(m):
        d[i][j] *= max_g

print('Матрица d после изменения:')

for i in range(n):
    for j in range(m):
        print('{:<10.7g}'.format(d[i][j]), end='')
    print()
