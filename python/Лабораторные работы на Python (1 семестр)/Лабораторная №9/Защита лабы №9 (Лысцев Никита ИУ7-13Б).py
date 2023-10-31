n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

matrix = [[0] * m for i in range(n)]

print()
k = 1
for i in range(n - 1, -1, -1):
    j = m - 1
    if i % 2 != 0:
        while j > -1:
            matrix[i][m - 1 - j] = k
            k += 1
            j -= 1
    elif i % 2 == 0:
        while j > -1:
            matrix[i][j] = k
            k += 1
            j -= 1

for i in matrix:
    print(i)
