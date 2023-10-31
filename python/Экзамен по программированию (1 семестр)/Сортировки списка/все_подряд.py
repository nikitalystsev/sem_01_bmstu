def bubble_classic(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


def bubble_with_flag(a):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
    return a


def bubble_with_barrier(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def bubble_reverse_barrier(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


def shaker_sort(a):
    l = 0
    r = len(a) - 1
    while r > l:
        for i in range(l, r, 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        r -= 1

        for j in range(r, l, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]

        l += 1

    return a


def selection_sort(a):
    for i in range(len(a) - 1):
        i_min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[i_min]:
                i_min = j
        a[i], a[i_min] = a[i_min], a[i]

    return a


def simple_insertion(a):
    for index, temp in enumerate(a):
        while index - 1 >= 0 and temp < a[index - 1]:
            a[index] = a[index - 1]
            index -= 1
        a[index] = temp
    return a


def shell_sort(a):
    dist = len(a) // 2
    while dist:
        for index, temp in enumerate(a):
            while index - dist >= 0 and temp < a[index - dist]:
                a[index] = a[index - dist]
                index -= dist
            a[index] = temp
        dist = 1 if dist == 2 else int(dist * 5.0 / 11)
    return a


# def bin_insertion(data):
#     for i, temp in enumerate(data):
#         left, right = 0, i
#         while right > left:
#             mid = left + (right - left) // 2
#             if data[mid] <= temp:
#                 left = mid + 1
#             else:
#                 right = mid
#         for j in range(i, right, -1):
#             data[j] = data[j - 1]
#         data[right] = temp
#     return data


def bin_insertion1(a):
    for index, temp in enumerate(a):
        l, r = 0, index
        while r > l:
            mid = (r + l) // 2
            if temp >= a[mid]:
                l = mid + 1
            else:

                r = mid
        for i in range(index, r, -1):
            a[i] = a[i - 1]
        a[r] = temp
    return a


from random import randint


def quick_sort(a, l, r):
    if l >= r: return
    i, j = l, r
    x = a[randint(l, r)]
    while i <= j:
        while a[j] > x: j -= 1
        while a[i] < x: i += 1

        if j >= i:
            a[i], a[j] = a[j], a[i]
            j -= 1
            i += 1

        quick_sort(a, l, j)
        quick_sort(a, i, r)

    return a


q = [randint(0, 15) for _ in range(30)]

print(quick_sort(q, 0, len(q) - 1))