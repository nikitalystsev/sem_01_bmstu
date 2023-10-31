
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбов матрицы: '))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(int(input('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1))))

print('Матрица сейчас:')
for i in matrix:
    print(i)

sum_all_column = []
for j in range(m):
    column_j = []
    for i in range(n):
        print('Элемент столбца: ', matrix[i][j])
        column_j.append(matrix[i][j])
    print('Список из элементов {}-го столбца: '.format(j), column_j)
    sum_column_j = sum([elem if abs(elem) != elem else 0 for elem in column_j])
    sum_all_column.append(sum_column_j)

print('Список сумм всех столбцов: ', sum_all_column)

if min(sum_all_column) == 0:
    print('В матрице нет отрицательных элементов, переставлять нечего')
else:
    c = 0
    for i in range(1, len(sum_all_column)):
        if abs(sum_all_column[i]) != sum_all_column[i]:
            c += 1
        if sum_all_column[i] < sum_all_column[i - 1] and sum_all_column[i] != 0:
            index_min = i
        if sum_all_column[i] > sum_all_column[i - 1] and sum_all_column[i] != 0:
            index_max = i
    if c == 1:
        print('Столбец с суммой отрицательных элементов всего один,'
              ' переставлять его с другим таким же столбцом невозможно')
    else:
        for i in matrix:
            i[index_min], i[index_max] = i[index_max], i[index_min]

print('Матрица после изменений:')
for i in matrix:
    print(i)
