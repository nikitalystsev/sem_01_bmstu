import copy

def replace_elem(a: list, ind_row: int, ind_column: int):
    a[ind_row] = ['#' for _ in range(len(a[0]))]
    for i in range(len(a)):
        a[i][ind_column] = '#'
    return a
            
def input_matrix():            
    n = int(input('Введите количество строк матрицы: '))
    m = int(input('Введите количество столбцов матрицы: '))
    matrix = [[input('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1)) for j in range(m)] for i in range(n)]
    return matrix

def print_matrix(matrix):
    for i in matrix:
        print(i)


def ar_mean(matrix):
    vector = []
    for j in range(len(matrix[0])):
        column = []
        for i in range(len(matrix)):
            elem = matrix[i][j]
            if elem.isdigit():
                column.append(int(elem))
        if len(column) != 0:
            ar_mean_ = sum(column) / len(column)
            vector.append(ar_mean_)
    return vector

def main():
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    matrix = input_matrix()
    other_matrix = copy.deepcopy(matrix)
    print_matrix(matrix)
    vector = ar_mean(matrix)
    print('Список с арифметическими значениями:', vector)
    for i in range(len(other_matrix)):
        for j in range(len(other_matrix[0])):
            elem = list(other_matrix[i][j])
            for index_elem in range(len(elem)):
                if elem[index_elem] in alp:
                    matrix = replace_elem(matrix, i, j)
                    break
    print_matrix(matrix)

main()



