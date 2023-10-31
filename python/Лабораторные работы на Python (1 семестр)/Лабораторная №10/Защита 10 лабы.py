# метод срединных прямоугольников
n = int(input('Введите количество разбиений: '))
a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))


def f(x):
    return 2 * x


h = (b - a) / n
x2 = a
area = 0
for i in range(n):
    x1 = x2
    x2 = a + (i + 1) * h
    x = (x1 + x2) / 2
    area += f(x)
integral = area * h

print('Интеграл равен: ', integral)
