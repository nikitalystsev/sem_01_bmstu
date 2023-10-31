n = int(input('Введите размер матрицы: '))
matrix = [[int(input('Введите {}-й элемент {}-й строки: '.format(j + 1, i + 1))) for j in range(n)] for i in range(n)]
print('Введенная матрица:')
for row in matrix:
    print(row)
print()    
count_elem = []    
for i in range(n):
    count = 0
    elem = matrix[i][i] 
    for j in range(n):
        if matrix[i][j] > elem:
            count += 1
    count_elem.append(count)

print('Список с количествами элементов в строке, которые больше элемента на главной диагонали:')
print(count_elem)
            
            
            
        
