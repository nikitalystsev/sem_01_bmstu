# удалить из целочисленной матрицы все столбцы,
# среднее арифметическое значение положительных элементов в которых меньше 10.

n = int(input('Введите количество строк в матрице: '))
m = int(input('Введите количество столбцов в матрице: '))
matrix = [[int(input('Введите элемент матрицы: ')) for j in range(m)] for i in range(n)]

for i in matrix:
    print(i)

ar_mean_coll = []
for j in range(m):
    sum_elem = 0
    c = 0
    i = 0
    for i in range(n):
        elem = matrix[i][j]
        if elem > 0:
            sum_elem += elem
            c += 1
    if c != 0:
        ar_mean = sum_elem / c
        ar_mean_coll.append(ar_mean)
    else:
        ar_mean_coll.append(100)

for i in matrix:
    j = 0
    while j < len(i):
        if ar_mean_coll[j] < 10:
            del i[j]
            j = j
        else:
            j += 1

for i in matrix:
    print(i)
