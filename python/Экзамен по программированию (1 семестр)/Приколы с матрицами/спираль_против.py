def foo(x: int):
    i = j = 0
    a[0][0] = x
    x -= 1
    while x > 0:
        while j + 1 < N and a[i][j + 1] == 0:
            a[i][j + 1] = x
            x -= 1
            j += 1

        while i + 1 < N and a[i + 1][j] == 0:
            a[i + 1][j] = x
            x -= 1
            i += 1
        while a[i - 1][j - 1] == 0:
            a[i - 1][j - 1] = x
            x -= 1
            i -= 1
            j -= 1


N = int(input('Введите N: '))
a = [[0 for _ in range(N)] for _ in range(N)]

# for i in range(N):
#     print(a[i])

x = N * (N + 1) // 2
foo(x)

for i in range(N):
    print(a[i])


def foo(x_max, matrix):
    i = j = len(matrix)-1
    x = x_max
    matrix[i][j] = x_max
    x -= 1
    while x > 0:
        while j-1 >= 0 and matrix[i][j-1] == 0:
            matrix[i][j-1] = x 
            x -= 1
            j -= 1

        while i - 1 >= 0 and matrix[i-1][j] == 0:
            matrix[i-1][j] = x
            x -= 1
            i -= 1

        while j + 1 < len(matrix) and matrix[i][j+1] == 0:
            matrix[i][j+1] = x
            x -= 1
            j += 1

        while i + 1 < len(matrix) and matrix[i+1][j] == 0:
            matrix[i+1][j] = x
            x -= 1
            i += 1

matrix_size = int(input('Введите размерность: '))
matrix_initialisation = [[0 for _ in range (matrix_size)] for _ in range (matrix_size)]

foo(matrix_size**2, matrix_initialisation)

for i in matrix_initialisation:
    print (i)