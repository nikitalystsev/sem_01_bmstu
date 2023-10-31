k = int(input('Введите размерность списка кортежей:'))
list_tuples = []
a = ('R', 'G', 'B', 'Y', 'W', 'P')
for i in range(k):
    elem_tuple_1, elem_tuple_2 = input('Введите элементы кортежа через пробел: ').split()
    elem_tuple_1 = int(elem_tuple_1)
    input_tuple = (elem_tuple_1, elem_tuple_2)
    list_tuples.append(input_tuple)

print('Введенный список:')
for tuple_elem in list_tuples:
    print(tuple_elem)
print()


def that_more(b: str, c: str):
    min_len_str = min(len(b), len(c))
    for index_elem in range(min_len_str):
        ind_alpha_elem_1 = a.index(b[index_elem])
        ind_alpha_elem_2 = a.index(c[index_elem])
        if b[index_elem] != c[index_elem]:
            if ind_alpha_elem_1 > ind_alpha_elem_2:
                print('зашло в первое')
                return True
            elif ind_alpha_elem_1 < ind_alpha_elem_2:
                print('зашло вообще непонятно куда')
                return False
    if len(b) > len(c):
        print('зашло во второе')
        return True
    print('никуда не зашло')
    return False


for i in range(len(list_tuples) - 1):
    for j in range(len(list_tuples) - 1 - i):

        if list_tuples[j][0] > list_tuples[j + 1][0]:
            list_tuples[j], list_tuples[j + 1] = list_tuples[j + 1], list_tuples[j]

        if list_tuples[j][0] == list_tuples[j + 1][0]:
            if that_more(list_tuples[j][1], list_tuples[j + 1][1]):
                list_tuples[j], list_tuples[j + 1] = list_tuples[j + 1], list_tuples[j]

print('Отсортированный список:')
for tuple_elem in list_tuples:
    print(tuple_elem)
print()
