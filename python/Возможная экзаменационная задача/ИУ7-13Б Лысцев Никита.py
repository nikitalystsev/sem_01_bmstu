import math as m

f = open('in.txt', 'r+')
f_2 = open('out.txt', 'w')
while True:
    string = f.readline()
    if not string:
        break
    list_string = string.split('.')
    flag = True
    if list_string[0][0] == '-':
        whole_part = list_string[0][1:]
        flag = False
    else:
        whole_part = list_string[0]
    fraction = list_string[1].rstrip('\n')
    whole_part = [i for i in whole_part]
    fraction = [i for i in fraction]

    # перевод в 10 сс
    for i in range(len(whole_part)):
        whole_part[i] = int(whole_part[i]) * (8 ** (len(whole_part) - (i + 1)))
    for i in range(len(fraction)):
        fraction[i] = int(fraction[i]) * (8 ** (-(i + 1)))
    sum_whole_part = sum(whole_part)
    sum_fraction = sum(fraction)

    # перевод целой часть в 16 сс
    whole_part = hex(sum_whole_part)
    whole_part = whole_part[2:]

    # перевод дробной часть в 16 сс
    a = ''
    number = sum_fraction

    count_iteration = 0
    while m.modf(number)[0] != 0.0:
        number *= 16
        if m.modf(number)[1] == 10.0:
            a += 'a'
        elif m.modf(number)[1] == 11.0:
            a += 'b'
        elif m.modf(number)[1] == 12.0:
            a += 'c'
        elif m.modf(number)[1] == 13.0:
            a += 'd'
        elif m.modf(number)[1] == 14.0:
            a += 'e'
        elif m.modf(number)[1] == 15.0:
            a += 'f'
        else:
            a += str(int(m.modf(number)[1]))
        count_iteration += 1
        number = m.modf(number)[0]

    fraction = '.' + a
    if not flag:
        number = '-' + str(whole_part) + fraction
    else:
        number = str(whole_part) + fraction
    if '\n' not in number:
        number += '\n'
    f_2.write(number)

f_2.close()
f.close()

# собственно процесс сортировки
f_3 = open('out2.txt', 'w')
f_2 = open('out.txt', 'r')
max_len = 0
while True:
    string = f_2.readline()
    if not string:
        break
    if len(string) > max_len:
        max_len = len(string)
f_2.close()
print('длина максимально длинной строки:', max_len)

for i in range(1, max_len + 1):
    f_2 = open('out.txt', 'r')
    while True:
        string = f_2.readline()
        if not string:
            break
        if len(string) == i:
            f_3.write(string)
    f_2.close()











