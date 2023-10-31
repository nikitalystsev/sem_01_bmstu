def foo(x_max: int, a: list):
    i = j = 0
    x = 1
    a[0][0] = x
    x += 1
    while x <= x_max:
        while j + 1 < n and a[i][j + 1] == 0:
            a[i][j + 1] = x
            x += 1
            j += 1

        while i + 1 < n and j - 1 >= 0 and a[i + 1][j - 1] == 0:
            a[i + 1][j - 1] = x
            x += 1
            j -= 1
            i += 1

        while a[i - 1][j] == 0:
            a[i - 1][j] = x
            i -= 1
            x += 1


n = int(input('Input size of square matrix: '))
matrix = [[0] * n for _ in range(n)]
x = n * (n + 1) // 2

foo(x, matrix)
for i in range(n):
    print(matrix[i])


def foo(x_max):
    i = j = 0
    x = 1
    a[0][0] = x
    x += 1

    while x <= x_max:
        while j + 1 < n and a[i][j + 1] == 0:
            a[i][j + 1] = x
            x += 1
            j += 1

        while i + 1 < n and a[i + 1][j] == 0:
            a[i + 1][j] = x
            x += 1
            i += 1

        while j - 1 >= 0 and a[i][j - 1] == 0:
            a[i][j - 1] = x
            x += 1
            j -= 1

        while a[i - 1][j] == 0:
            a[i - 1][j] = x
            x += 1
            i -= 1


n = int(input('Введите размер матрицы: '))

a = [[0] * n for _ in range(n)]
foo(n * n)

for k in range(n):
    print(a[k])