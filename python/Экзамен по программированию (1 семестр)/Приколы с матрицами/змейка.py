def snake_matrix(matrix):
    x = 1
    i = j = 0
    matrix[0][0] = x

    while i < len(matrix):
        while j + 1 < len(matrix) and matrix[i][j+1] == 0:
            if j == 0:
                matrix[i][0] = x
                x += 1
            matrix[i][j+1] = x
            x += 1
            j += 1
        i += 1

        if i < len(matrix):
            while j - 1 >= 0 and matrix[i][j-1] == 0:
                if j == len(matrix) - 1:
                    matrix[i][len(matrix)-1] = x 
                    x += 1
                matrix[i][j-1] = x
                x += 1
                j -= 1
            i += 1

matrix_size = int(input('Enter size: '))
matrix_array = [[0 for _ in range (matrix_size)] for _ in range (matrix_size)]

snake_matrix(matrix_array)

for i in matrix_array:
    print (i)