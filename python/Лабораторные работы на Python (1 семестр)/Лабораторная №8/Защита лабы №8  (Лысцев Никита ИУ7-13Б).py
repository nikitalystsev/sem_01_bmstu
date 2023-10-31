n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))
matrix = [[int(input('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1))) for j in range(m)] for i in range(n)]
print('Введенная матрица: ')
for i in matrix:
    print(i)
print()

elem_1 = matrix[0][0]

c = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == elem_1:
            c += 1

if c != n * m:
    print('В матрице не все элементы одинаковые.')
    print()
    min_i = 0
    min_j = 0
    max_i = 0
    max_j = 0
    for i in range(n):
        for j in range(m):
            elem = matrix[i][j]
            if elem < matrix[min_i][min_j]:
                min_i = i
                min_j = j
            if elem > matrix[max_i][max_j]:
                max_i = i
                max_j = j
    matrix[max_i][max_j], matrix[min_i][min_j] = matrix[min_i][min_j], matrix[max_i][max_j]
    print('Измененная матрица: ')
    for i in matrix:
        print(i)
else:
    print('В матрице все элементы одинаковые.')
