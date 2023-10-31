

a, b, h = map(float, input('Введите начальное, конечное значение аргумента и шаг через пробел: ').split())

count_iter = int((b - a) / h) + 1
x = a
max_y = float("-inf")
min_y = float("inf")
for i in range(count_iter):
    y = abs(x) - 1
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y    
    x = a + (i + 1) * h
x = a
width = 80
scale = (max_y - min_y) / width

for j in range(count_iter):
    abscissa = '| {:^10.4g}|'.format(x)
    y = abs(x) - 1

    distan = int(abs(y - min_y) / scale)
    graph = ' ' * (width - 1)
    intersec = int(abs(0 - min_y) / scale)
    graph = graph[:distan] + '*' + graph[distan + 1:]
    if min_y <= 0 and max_y >= 0:
        if graph[intersec] == '*':
            graph = graph[:intersec] + 'x' + graph[intersec + 1:]
        else:
            graph = graph[:intersec] + '|' + graph[intersec + 1:] 
    abscissa += graph
    x = a + (j + 1) * h           
    print(abscissa)