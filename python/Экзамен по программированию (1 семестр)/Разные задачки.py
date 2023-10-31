##n = int(input('Введите размер списков: '))
##a = [int(input('Введите целое число: ')) for i in range(n)]
##b = [int(input('Введите целое число: ')) for i in range(n)]
##print('Введенные списки:')
##print(a)
##print(b)
##print()
##c = [i + j for i, j in zip(a, b)]
##print(*c)

##a = list(map(int, input('Введите целые числа через пробел: ').split()))
##c = 0
##for i in range(len(a)):
##    if a[i] % 2 != 0:
##        c += a[i]
##print(c)

##a = list(input('Введите название городов через пробел: ').split())
##print('Список с названиями городов:')
##print(a)
##print()
##for i in range(len(a)):
##    a[i] = len(a[i])
##print('Список с  длиной названий городов:')
##print(a)

##n = int(input('Введите натуральное число: '))
##a = set()
##for i in range(1, int(n ** 0.5) + 1):
##    if n % i == 0:
##        a.add(i)
##        a.add(n // i)
##
##for i in a:
##    print(i)

##k = 1
##a = [[0] * 4 for i in range(4)]
##print('Созданная матрица:')
##for i in a:
##    print(i)
##print()
##
##for i in range(len(a)):
##    for j in range(i, len(a)):
##        a[i][j] = k
##        k += 1

##for i in range(len(a)):
##    for j in range(len(a) - i):
##        a[i][j] = k
##        k += 1

##for i in range(len(a)):
##    for j in range(i + 1):
##        a[i][j] = k
##        k += 1

##for i in range(len(a)):
##    for j in range(len(a) - 1 - i, len(a)):
##        a[i][j] = k
##        k += 1
        
        
##print('Верхнетреугольная матрица:')
##for i in a:
##    print(i)
##    
##def func():
##    return 
##b = func()
##print(b)
##print(type(b))

##def f(x):
##    return x + 3
##
##def g(function, x):
##    return function(x) * function(x)
##
##print(g(f, 7))

##def sample_decorator(func):
##    def wrapper():
##        print('Я родился...')
##        func()
##        print('Меня зовут Лунтик!')
##    return wrapper
##
##@sample_decorator
##def say():
##    print('Привет Мир.')
##
##say()

##f = open('in.txt')
### 1 способ чтения
##content = f.read()
### 2 способ чтения
##lines_list = f.readlines()
### 3 способ чтения
##for i in range(5):
##    string = f.readline()
### 4 способ чтения
##for s in f:
##    print(s)
##
##f.close()
##
##
##f = open('in.txt', 'w')
### 1 способ записи
##f.write('abcd')
##
### 2 способ записи
##f.writelines(['1', 'abcd'])
##
### 3 способ записи
##print('def', file=f)
##
##f.close()
#### нет символа перевода строки
##
### first:
##string = f.readline()
##while string != '':
##    
### second:
##while True:
##    string = f.readline()
##    if not string:
##        break
### third:
##for s in f:
##    print(s)
##
##
##def f():
##    for i in [1, 2, 3, 4, 5, 6, 7]:
##        yield i
##        
##print('first')
##for i in f():
##    print(i)
##    
##print('second')
##for i in f():
##    print(i)
##import numpy as np
####data = [i for i in range(1, 6)]
####
####arr = np.array(data)
####
####print(arr)
####print(arr.shape)
####print(arr.dtype)
####print(arr.ndim)
##
##dtype = [('weight',int), ('height',float), ('age', int)]
##v = [(70, 1.75, 15), (65, 1.8, 19), (45, 1.85, 16)]
##c = np.array(v, dtype=dtype)
##c.sort(axis=1, order = ['weight'])
##print(c)

##import matplotlib.pyplot as plt

##x = [0, 6, 11, 17, 24, 31, 38, 40]
##y = [0, 2, 13, 10, 16, 12, 20, 30]
##plt.axis([0,10,0,20])
##plt.axis('equal')
##plt.title('Graphic points $x^2$') #, fontsize=14, ha='left', va='baseline')
##plt.plot(x, y, '-', linewidth=3.5)
##plt.xlabel('x')
##plt.ylabel('y $f(x)$')
##plt.grid(True)
##plt.show()

##x = [0, 6, 11, 17, 24, 31, 38, 40]
##y = [0, 2, 13, 10, 16, 12, 20, 17]
##plt.plot(x, y)
##plt.xticks(range(0, len(x) + 33, 5),['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'w'])
##plt.yticks(range(0, 23, 4))
##plt.grid(True)
##plt.show()

##import numpy as np
##import matplotlib.pyplot as plt
##
##
##x = np.linspace(-5, 5, 2000)
##y = np.sin(x)
##plt.axis('equal')
##plt.plot(x, y, 'r>')
##plt.grid(True)
##plt.show()

##import numpy as np
##import matplotlib.pyplot as plt
##
##x1 = np.linspace(-10, 10, 100) #массив абсцисс для графиков синуса, косинуса и экспоненты
##
##x4 = np.linspace(-2, 2, 10) #массив абсцисс для графика модуля
##
##y1 = np.sin(x1)
##
##y2 = np.cos(x1)
##
##y3 = x1**2 * np.exp(-x1**2)
##
##y4 = abs(x4)
##plt.legend(loc='upper left') 
##
##plt.plot(x1, y1, '--', label='sin(x)') #штриховая линия
##
##plt.plot(x1, y2, label='cos(x)')
##
##plt.plot(x1, y3, '-.', label='x**2*exp(-x**2)') #штрих-пунктир
##
##
###plt.plot(x1, y3, '-.', label='$x^2 exp(-x^2)$')
##plt.plot(x4, y4, ':', linewidth=3, label='|x|') #пунктирная, толщиной 5
##plt.title('4 graphs') #
##plt.xlabel('X') #
##plt.ylabel('Y') #
##plt.legend(loc=2) #
##plt.grid() #
##plt.show()
##
##import numpy as np
##import matplotlib.pyplot as plt
##
##x1 = np.linspace(0, 6, 100)
##plt.figure(1)
##plt.plot(x1, np.sin(x1))
##plt.grid(True)
##plt.title('$sin(x)$')
##x2 = np.linspace(-6, 10, 100)
##
##plt.figure(2)
##plt.plot(x2, x2*x2)
##plt.grid(True)
##plt.title('$x^2$')
##plt.show()

##import numpy as np
##import matplotlib.pyplot as plt
##
##
##x1 = np.linspace(0, 6, 100)
##plt.subplot(221)
##plt.plot(x1, np.sin(x1))
##plt.axis('equal')
##plt.grid(True)
##plt.title('$sin(x)$')
##
##x2 = np.linspace(-6, 10, 100)
##plt.subplot(222)
##plt.plot(x2, x2*x2, 'g')
##plt.grid(True)
##plt.title('$x^2$')
##
##x3 = np.linspace(-10, 10, 100)
##t = np.arange(-10, 11,1)
##plt.subplot(223)
##plt.plot(x3, x3*x3,'y', t, t*t, 'ro')
##plt.title('$x^2$')
##
##x4 = np.linspace(-10, 10, 100)
##plt.subplot(224)
##plt.plot(x4, -x4, 'y')
####plt.subplot(224).spines['left'].set_position('center')
####plt.subplot(224).spines['bottom'].set_position('center')
##plt.grid(True)
##plt.title('$-x$')
##plt.show()

##
##import matplotlib.pyplot as plt
##import numpy as np
##
##x = np.random.normal(0, 3, 1000)# np.random.randn(1000)
##plt.hist(x,25) # по умолчанию 10
##plt.show()

##import matplotlib.pyplot as plt
##
##x = [6, 12, 20, 7, 5, 5]
##
##languages = ['Matlab', 'Java', 'Python', 'C', 'C++', 'Other']
##
##plt.figure(figsize=(5,9))
##explode = [0, 0, 0.2, 0, 0.3, 0]
##plt.pie(x, labels = languages, explode=explode, autopct='%1.1f%%', shadow=False)
##plt.title('Circle diagram')
##plt.show()

##import random as rd
##
##a = [rd.randint(-1000, 1000) for _ in range(10)]
##print('Изначальный список:', a, sep='\n')

### Сортировка вставками:
##for i in range(1, len(a)):
##    for j in range(i, 0, -1):
##        if a[j] < a[j - 1]:
##            a[j], a[j - 1] = a[j - 1], a[j]
##        else:
##            break
##
##print('Отсортированный список:', a, sep='\n')

### Сортировка выбором:
##for i in range(len(a) - 1):
##    min_elem = a[i]
##    min_ind = i
##    for j in range(i + 1, len(a)):
##        if a[j] < min_elem:
##            min_elem = a[j]
##            min_ind = j
##    if min_ind != i:
##        a[i], a[min_ind] = a[min_ind], a[i]
##        
##print('Отсортированный список:', a, sep='\n')


### Сортировка вставками с бинарным поиском:
##for i in range (1, len(a)):
##    elem = a[i]
##    left_border = 0
##    right_border = i
##    if left_border == right_border:
##        left_border += 1
##    else:
##        while left_border < right_border:
##            mid = (left_border + right_border) // 2
##            if elem < a[mid] : 
##                right_border = mid
##            else: left_border = mid + 1
##    j = i 
##    while (j > left_border and j > 0):
##        a[j] = a[j-1]
##        j -= 1
##    a[left_border] = elem
##
##print('Отсортированный список:', a, sep='\n')           
    
        
### Сортировка вставками с барьером:
##def insertion_barrier_sorting(arr):
##     arr = [0] + arr
##     for i in range (1, len(arr)):
##         arr[0] = arr[i]
##         j = i - 1
##         while arr[0] < arr[j]:
##             arr[j+1] = arr[j]
##             j -= 1
##         arr[j+1] = arr[0]
##     return arr[1:]
##a = insertion_barrier_sorting(a)
##print('Отсортированный список:', a, sep='\n')
    
### Сортировка Шелла
##def shell_sort(data: list):
##    last_index = len(data) - 1
##    step = len(data) // 2
##    while step > 0:
##        for i in range(step, last_index + 1, 1):
##            j = i
##            delta = j - step
##            while delta >= 0 and data[delta] > data[j]:
##                data[delta], data[j] = data[j], data[delta]
##                j = delta
##                delta = j - step
##        step //= 2
##    return data    
##a = shell_sort(a)
##print('Отсортированный список:', a, sep='\n')

### Сортировка пузырьком:
##for run in range(len(a) - 1):
##    for i in range(len(a) - 1 - run):
##        if a[i] > a[i + 1]:
##            a[i], a[i + 1] = a[i + 1], a[i]
##print('Отсортированный список:', a, sep='\n')       

### Сортировка пузырьком c с флагом:
##for run in range(len(a) - 1):
##    flag = True
##    for i in range(len(a) - 1 - run):
##        if a[i] > a[i + 1]:
##            a[i], a[i + 1] = a[i + 1], a[i]
##            flag = False
##    if flag:
##        break
##print('Отсортированный список:', a, sep='\n')       
        
### Шейкерная сортировка:
##left = 0
##right = len(a) - 1
##
##while left <= right:
##    for i in range(left, right, +1):
##        if a[i] > a[i + 1]:
##            a[i], a[i + 1] = a[i + 1], a[i]
##    right -= 1
##
##    for i in range(right, left, -1):
##        if a[i - 1] > a[i]:
##            a[i], a[i - 1] = a[i - 1], a[i]
##    left += 1
##print('Отсортированный список:', a, sep='\n')   

### Быстрая сортировка:
##def quick_sort(s):
##    if len(s) <= 1:
##        return s
##    rand_ind = rd.randint(0, len(s) - 1)
##    elem = s[rand_ind]
##    left = list(filter(lambda x: x < elem, s))
##    center = [i for i in s if i == elem]
##    right = list(filter(lambda x: x > elem, s))
##
##    return quick_sort(left) + center + quick_sort(right)
##a = quick_sort(a)
##print('Отсортированный список:', a, sep='\n')

##n = int(input('Введите количество строк матрицы: '))
##m = int(input('Введите количество столбцов матрицы: '))
##a = [[int(input('Введите элемент матрицы: ')) for j in range(m)] for i in range(n)]
##
##for i in a:
##    print(i)
##
##def transpose(matr):
##    rez = []
##    for j in range(m):
##        tmp = []
##        for i in range(n):
##            tmp += [matr[i][j]]
##        rez.append(tmp)
##    return rez
##
##        
##a = transpose(a)       
##        
##for i in a:
##    print(i)

##def func():
##    for i in range(5):
##        yield i
##a = func()
##print(a)
##for elem in a:
##    print(elem)

##a = input('Введите строку: ')
##c = 1
##c1 = 1
##for i in range(len(a) - 1):
##    if a[i] == a[i + 1] == ' ':
##        c += 1
##        c1 = max(c, c1)
##    else:
##        c = 1
##if c1 != 1:
##    print('Максимальное количество подряд идущих пробелов в строке:', c1)
##else:
##    print('Максимальное количество подряд идущих пробелов в строке:', c1 - 1)

##n = int(input('Введите количество элементов: '))
##a = []
##for i in range(n):
##    a.append(float(input('Введите вещественное  число: ')))
##print('Введенный  список:', a)
##for i in range(len(a)):
##    if a[i] < 0:
##        a[i] += 0.5
##    else:
##        middle = sum(a) / len(a)
##        if a[i] < middle:
##            a[i] = 0.1
##print('Среднее арифметическое:', sum(a) / len(a))
##print('Измененный список:', a)

##n = int(input('Введите количество элементов: '))
##a = []
##for i in range(n):
##    a.append(int(input('Введите число: ')))
##print('Введенный  список:', a)
##sum1 = 0
##c1 = 0
##c2 = 0
##for i in range(len(a)):
##    if a[i] > 0:
##        sum1 += a[i]
##    elif a[i] < 0:
##        c1 += 1
##    else:
##        c2 += 1
##print('сумма положительных:', sum1, 'число отрицательных:', c1, 'число нулевых:', c2, sep='\n')

##n = input('Введите строку: ')
##len_n = len(n)
##alp = 'аАбБвВгГдДЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъыЫьЬЭэЮюЯя'
##rus = []
##for i in range(len_n):
##    if n[i] in alp:
##        rus.append(n[i])
##if rus:
##    for i in range(1, len(rus)):
##        for j in range(i, 0, -1):
##            if alp.index(rus[j]) < alp.index(rus[j - 1]):
##                rus[j], rus[j - 1] = rus[j - 1], rus[j]                
##    print('Список русских букв в алфавитном порядке:', rus)
##else:
##    print('Русских букв в строке нет')

##n = input('Введите строку:')
##numb = '0123456789'
##numb_in_n = ''
##other_in_n = ''
##for i in range(len(n)):
##    if n[i] in numb:
##        numb_in_n += n[i]
##    else:
##        other_in_n += n[i]
##if numb_in_n:
##    print('цифры в тексте:', numb_in_n)
##else:
##    print('цифр в тексте нет')
##if other_in_n:
##    print('остальные литералы с сохранением взаимного расположения:', other_in_n)
##else:
##    print('остальных литералов в строке нет')

##n = input('Введите строку:')
##n = ''.join(list(reversed(n)))
##
##print('буквы строки в обратном порядке:', n, sep='\n')

##a = input('Введите строку: ')
##alp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
##
##flag = True
##for i in range(len(a) - 1):
##    if alp.index(a[i]) > alp.index(a[i + 1]):
##        flag = False
##if flag:
##    print('Буквы с строке упорядочены по алфавиту')
##else:
##    print('Буквы с строке  НЕ упорядочены по алфавиту')
    
               
##a = input('Введите строку: ')
##
##for i in range(len(a)):
##    if a[i] == a[i].upper():
##        a = a[:i] + a[i].lower() + a[i + 1:]
##print('Измененная строка:', a)


##n = input('Введите слова:')
##array_n = n.split()
##c = True
##for i in array_n:
##    if sorted(set(i)) == sorted(i):
##        print('слово из неповторяющихся символов:', i)
##        c = False
##if c:
##    print('слов с неповторяющимися символами не нашлось')

##def f(a: list, ind: int):
##    c1 = 0
##    c2 = 0
##    for i in range(ind + 1, len(a)):
##        if abs(a[i]) > abs(a[ind]):
##            c1 += 1
##    for i in range(ind - 1, -1, -1):
##        if abs(a[i]) < abs(a[ind]):
##            c2 += 1
##    return c1, c2
##
##n = list(map(int, input('введите список через пробел: ').split()))
##array = []
##
##for i in range(len(n)):
##    rez = f(n, i)
##    array.append(rez)
##
##print('Введенный список:', n)
##print('Список с количествами элементов:', array)

##a = [3] * 10
##
##def max_elem(a: list):
##    max_el = a.index(max(a))
##    return max_el
##
##def min_elem(a: list):
##    min_el = a.index(min(a))
##    return min_el
##
##n1 = max_elem(a)
##n2 = min_elem(a)
##if n1 > n2:
##    left = a[:n2]
##    center = a[n2 + 1: n1]
##    right = a[n1 + 1:]
##else:
##    left = a[:n1]
##    center = a[n1 + 1: n2]
##    right = a[n2 + 1:]
##
##print('Левая часть', left)
##print('Центр:', center)
##print('Правая часть', right)
##
##print('Сумма в левой части массива:', sum(left))
##print('Сумма в центре:', sum(center))
##print('Сумма в правой части массива:', sum(right))

##s = int(input('введите число:'))
##a = [[j for j in range(7)] for i in range(4)]
##b = [[j for j in range(7)] for i in range(4)]
##for i in a:
##    print(i)
##
##def f(a: list, ind1: int, ind2: int):
##    sum_elem = 0
##    for i in range(ind1 - 1, ind1 + 1 + 1):
##        for j in range(ind2 - 1, ind2 + 1 + 1):
##            if i >= 0 and i <= 3 and j >= 0 and j <= 6:
##                sum_elem += a[i][j]
##    return sum_elem
##
##for i in range(len(a)):
##    for j in range(len(a[i])):
##        sum_elem = f(a, i, j)
##        if sum_elem < s:
##            b[i][j] = True
##        else:
##            b[i][j] = False
##for i in b:
##    print(i)

def dimen():
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))
    return n, m

def input_matr(n, m):
    a = [[int(input('Введите челое число: ')) for j in range(n)] for i in range(m)]
    b = [[int(input('Введите челое число: ')) for j in range(n)] for i in range(m)]
    c = [[0 for j in range(n)] for i in range(m)]
    return a, b, c

def get_col(b: list, ind: int):
    col = [b[i][ind] for i in range(len(b))]
    return col

def ch_el(elem: int, column: list):
    if elem not in column:
        return True
    return False

def count_sum(a: list, b: list, ind: int):
    elem = 0
    for i in range(len(a)):
        elem += a[i] if ch_el(a[i], get_col(b, ind)) else 0
    return elem
n, m = dimen()
a, b, c = input_matr(n, m)

print('матрица a:')
for i in a:
    print(i)
print()

print('матрица b:')
for i in b:
    print(i)
    
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = count_sum(a[i], b, j)
print()

print('матрица с:')
for i in c:
    print(i)
        

        
                   
    
    
    
    





                
            
            
    
                   
            
                       
                       
    
    
    
    

            


            
            
    
            
            
    
    
               
    
        
