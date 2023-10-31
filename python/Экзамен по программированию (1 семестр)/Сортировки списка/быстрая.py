import random as r
def quick_sort(arr, start = 0, end = None):
    if len(arr) == 0:
        return arr
    pind = r.randint(start, end-1)
    pivot = arr[pind]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left, 0, len(left)) + [pivot] + quick_sort(right, 0, len(right))

s = [4, 8, 2, 9, 5, 1]
print (quick_sort(s))