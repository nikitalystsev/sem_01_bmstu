# Лысцев Н.Д. ИУ7-13Б
# Замена в матрице всех гласных английских букв на точки
#
# Ввод:
# матрица символов
#
# Вывод:
# матрица до и после изменений

import checks as ch

while True:
    n = ch.clever_input('Введите количество строк матрицы: ')
    if n <= 0:
        print('Неверный ввод! Количество строк не может быть меньше нуля или равняться нулю.')
    else:
        break

while True:
    m = ch.clever_input('Введите количество столбцов матрицы: ')
    if m <= 0:
        print('Неверный ввод! Количество столбцов не может быть меньше нуля или равняться нулю.')
    else:
        break

matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        while True:
            symbol = input('Введите {}-й элемент {}-й строки матрицы d: '.format(j + 1, i + 1))
            if len(symbol) != 1:
                print('Так как матрица символьная, то пжалуйста, введите всего один символ.')
            else:
                break
        matrix[i].append(symbol)


vowels = 'AaEeIiOoUuYy'

print('Матрица до изменений:')
for i in matrix:
    print(i)

print()

for i in range(n):
    for j in range(m):
        elem = matrix[i][j]
        if elem in vowels:
            elem = '.'
            matrix[i][j] = elem

print('Матрица после изменений: ')
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end='')
    print()
