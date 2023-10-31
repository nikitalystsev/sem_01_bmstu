# Лысцев Н.Д. ИУ7-13Б
# Транспонирование квадратной матрицы
#
# Ввод:
# размер матрицы и сама матрица
#
# Вывод:
# в зависимости от входных данных выводится  либо только введенная матрица,
# либо и введенная и транспонированная матрицы


import checks as ch

while True:
    n = ch.clever_input('Введите размер матрицы: ')
    if n <= 0:
        print('Неверный ввод! Размер матрицы не может быть меньше нуля или равняться нулю.')
    else:
        break

if n == 1:
    matrix = [[ch.clever_input_2('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1)) for j in range(n)] for i in
              range(n)]
    print('Размер матрицы равен 1. Транспонирование не изменит матрицу.')
    print('Введенная матрица: ')
    print(*matrix)
else:
    matrix = [[ch.clever_input_2('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1)) for j in range(n)] for i in
              range(n)]
    print('Введенная матрица до транспонирования: ')
    for i in range(n):
        for j in range(n):
            print('{:<10.7g}'.format(matrix[i][j]), end='')
        print()

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print('Введенная матрица после транспонирования: ')
    for i in range(n):
        for j in range(n):
            print('{:<10.7g}'.format(matrix[i][j]), end='')
        print()
