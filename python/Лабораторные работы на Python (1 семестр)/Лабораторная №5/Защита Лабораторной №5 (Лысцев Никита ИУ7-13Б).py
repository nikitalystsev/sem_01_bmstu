x = float(input('Введите значение аргумента: '))
eps = float(input('Введите требуемую точность вычисления: '))

n = 1
m = 1
b = x ** 3
t = float("inf")
new_x = x
k = 1
s = 0
while abs(t) > eps:
    t = (((-1) ** n) * b) / m
    s += t
    n += 1
    k += 1
    m *= k
    
    b = b * (new_x ** 2)

print('Вычисленная сумма равна: {:10.4g}'.format(s))