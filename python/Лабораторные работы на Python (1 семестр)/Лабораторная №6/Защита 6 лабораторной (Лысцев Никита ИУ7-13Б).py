a = list(map(int, input('Введите элементы списка через пробел: ').split()))
b = list(map(int, input('Введите элементы списка через пробел: ').split()))
c = list(map(int, input('Введите элементы списка через пробел: ').split()))
print('Список а: ', a)
print('Список b: ', b)
print('Список c: ', c)
d = []
for i in range(len(a)):
    if (a[i] not in b) and (a[i] not in c):
        d.append(a[i])
print('Конечный неразвернутый список: ', d)
print('Конечный развернутый список: ', d[::-1])
