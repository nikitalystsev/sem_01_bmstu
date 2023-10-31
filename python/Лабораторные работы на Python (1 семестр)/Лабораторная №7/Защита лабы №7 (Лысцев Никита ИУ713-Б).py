def check_vowels(x: str):
    vowels = 'AaEeIiOoUuYy'
    for symbol in range(len(x)):
        if x[symbol] not in vowels:
            return False
    return True


a = []
n = int(input('Введите количество строк: '))
for i in range(n):
    a.append(input('Введите {}-ю строку: '.format(i + 1)))
print(a)
d = 0
for j in range(len(a)):
    if check_vowels(a[j]) and len(a[j]) > 0:
        d = j
        find_str = a[j]
        for i in range(d, -1, -1):
            a[i] = a[i - 1]
        a[0] = find_str


print(a)

