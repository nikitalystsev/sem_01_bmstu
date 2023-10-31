
# Функция
def f(x):
    return 5 * x

# Метод левых прямоугольников
def left_rectanglest(start, end, count):
    summ = 0 # Суммирование значений высот прямоугольников
    dx = (end - start) / count
    x_st = start 
    for i in range(count):
        summ += f(x_st + i * dx)
    return dx * summ 

# Mетод средних прямоугольников
def middle_rectangle(start, end, count):
    summ = 0
    dx = (end - start) / count
    x_st = start + 0.5 * dx
    for i in range(count):
        summ += f(x_st + i * dx)

    return summ * dx

# Mетод правых прямоугольников
def middle_rectangle(start, end, count):
    summ = 0
    dx = (end - start) / count
    x_st = start + dx
    for i in range(count):
        summ += f(x_st + i * dx)

    return summ * dx

# Метод трапеций
def trap(start, end, count):
    dx = (end - start) / count  
    summ = 0
    x_st = start
    while x_st < end:
        summ += ((func(x_st) + func(x_st + dx))/2) * dx
        x_start += dx
    
    return summ

# Метод парабол (чётное число интервалов)
def parab(start, end, count):
    dx = (end - start) / count
    summ = 0
    x_st = start
    while x_st < end:
        summ += (f(x_st) + 4*f(x_st + dx) + f(x_st + 2 * dx)) * 1/3 * dx
        x_start += 2 * dx
    
    return summ

# Метод Уэддля (число интервалов кратно 6)
def weddle(start, end, count):
    summ = 0
    dx = (end - start) / count
    x_st = start
    for i in range(count // 6):
        summ +=  (f(x_st) + 5 * f(x_st + dx) + f(x_st + 2 * dx) \
            + 6 * f(x_st + 3 * dx) + f(x_st + 4 * dx) + 5 * f(x_st + 5 * dx) + f(x_st + 6 * dx))
        x_st += 6 * dx  
    return 3/10 * dx * summ


# Метод 3/8 (число интервалов кратно 3)
def method_3_dev_8(start, end, count):

    dx = (end - start) / count
    summ = 0
    x_st = start
    for i in range(count // 3):
        summ +=  func(x_st) + 3 * func(x_st + dx) + 3 * func(x_st + 2 * dx) + func(x_st + 3 * dx)
        x_st += 3 * dx
    return 3/8 * dx * summ

 # Метод Буля (Число интервалов кратно 4)
def Boole(start, end, count):
    dx = (end - start) / count
    summ = 7 * (f(start) + f(end))
    
    for i in range(1, count // 4):
        summ += 32 * f(x_st + dx) + 12 * f(x_st + 2 * dx) + 32 * (x_st + 3 * dx) + 14 * (x_st + 4 * dx)
        x_st += 4 * dx
    return 2/45 * dx * summ


def Boole(start, end, count):
    dx = (end - start) / count
    summ = 7 * (f(start) + f(end))  # finish == start + h*n2

    s = 0
    for i in range(1, count, 2):
        s += f(start + dx * i)
    summ += 32 * s

    s = 0
    for i in range(2, count - 1, 4):
        s += f(start + dx * i)
    summ += 12 * s

    s = 0
    for i in range(4, count - 3, 4):
        s += f(start + dx * i)
    summ += 14 * s

    summ *= 2 * dx / 45
    return summ





