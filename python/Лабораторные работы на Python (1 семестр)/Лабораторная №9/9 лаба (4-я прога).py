# Лысцев Н.Д. ИУ7-13Б
# Поворот квадратной матрицы на 90 градусов по часовой стрелке, затем на 90
# градусов против часовой стрелки
#
# Ввод:
# размер матрицы и сама матрица
#
# Вывод:
# в зависимости от входных данных выводится  либо только введенная матрица,
# либо и введенная, и промежуточная, и конечная матрицы
import checks as ch

while True:
    n = ch.clever_input('Введите размер матрицы: ')
    if n <= 0:
        print('Неверный ввод! Размер матрицы не может быть меньше нуля или равняться нулю.')
    else:
        break

if n == 1:
    matrix = [[input('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1)) for j in range(n)] for i in
              range(n)]
    print('Размер матрицы равен 1. повороты на 90 градусов по и против часовой стрелки не изменят матрицу.')
    print('Введенная матрица: ')
    print(*matrix)
else:
    matrix = [[input('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1)) for j in range(n)] for i in
              range(n)]

    print('Введенная матрица до изменений:')
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end='\t')
        print()

    # по часовой
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            still_i = n - 1 - i
            still_j = n - 1 - j
            matrix[i][j], matrix[still_j][i], matrix[still_i][still_j], matrix[j][still_i] = matrix[still_j][i], \
                                                                                             matrix[still_i][
                                                                                                 still_j], \
                                                                                             matrix[j][still_i], \
                                                                                             matrix[i][j]

    print()

    print('Промежуточная матрица:')
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end='\t')
        print()

    # реально против часовой
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            still_i = n - 1 - i
            still_j = n - 1 - j
            matrix[i][j], matrix[j][still_i], matrix[still_i][still_j], matrix[still_j][i] = matrix[j][still_i], \
                                                                                             matrix[still_i][still_j], \
                                                                                             matrix[still_j][i], \
                                                                                             matrix[i][j]

    print()
    print('Матрица после изменений:')
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end='\t')
        print()
