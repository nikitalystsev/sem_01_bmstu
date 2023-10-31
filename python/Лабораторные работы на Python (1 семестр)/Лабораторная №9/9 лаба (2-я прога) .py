# Лысцев Н.Д. ИУ7-13Б
# Найти максимальное значение над главной диагональю и минимальное - под
# побочной диагональю
#
# Ввод:
# размер матрицы и сама матрица
#
# Вывод:
# в зависимости от входных данных выводится
# либо максимальный элемент над главной диагональю и минимальный под побочной,
# либо сама матрица
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
    print('Размер матрицы равен 1.'
          ' Максимального элемента над главной диагональю и минимального элемента под побочной диагональю нет.')
    print('Введенная матрица: ')
    print(*matrix)

else:
    matrix = [[ch.clever_input_2('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1)) for j in range(n)] for i in
              range(n)]
    print('Введенная матрица:')
    for i in range(n):
        for j in range(n):
            print('{:<5.7g}'.format(matrix[i][j]), end='')
        print()
    print()
    max_i_1 = 0
    max_j_1 = 1
    for i in range(n):
        for j in range(i + 1, n):
            elem = matrix[i][j]
            if elem > matrix[max_i_1][max_j_1]:
                max_i_1 = i
                max_j_1 = j
    print('Максимальный элемент над главной диагональю: ')
    print(matrix[max_i_1][max_j_1])
    print()
    min_i_2 = 1
    min_j_2 = n - 1
    for i in range(n):
        for j in range(n - i, n):
            elem = matrix[i][j]
            if elem < matrix[min_i_2][min_j_2]:
                min_i_2 = i
                min_j_2 = j
    print('Минимальный элемент под побочной диагональю: ')
    print(matrix[min_i_2][min_j_2])
