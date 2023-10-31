f = open('матрица.txt')
f_new = open('новая матрица.txt', 'w')
count_string = 0

while True:
    string = f.readline()
    if not string:
        break
    count_string += 1

f.close()

print('количество строк:', count_string)

for i in range(count_string):
    array_column = []
    f = open('матрица.txt')
    for j in range(count_string):
        string = f.readline()
        if string:
            string = string.strip('\n')
            str_matr = string.split()

                
            array_column += [str_matr[i]]
                
    print('список со столбцами:', array_column)
    transpose = ' '.join(array_column)
    if '\n' not in transpose:
        transpose += '\n'
    f_new.write(transpose)
    f.close()
f_new.close()
    
    
    

    
