a = []
d = ''
n = int(input('Введите количество строк: '))

for i in range(n):
    q = input('Введите строку: ')
    a.append(q)
g = float('-inf')

for i in a:
    if len(i) == 0:
        continue
    for j in range(len(i)):
        for k in range(len(i) + 1):
            b = i[j:k]
            if b == b[::-1] and b.isdigit() and len(b) >= 3:
                if len(i) > g:
                    g = len(i)
                    d = i

if not d:
    print('Строки с палиндромом не оказалось.')
else:
    print('Строка наибольшей длины с палиндромом: ', d)


