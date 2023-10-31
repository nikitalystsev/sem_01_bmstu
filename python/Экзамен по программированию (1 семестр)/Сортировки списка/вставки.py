# def insertion_sort(arr):
#     for i in range (1, len(arr)):
#         current_element = arr[i]
#         j = i - 1
#         while j >= 0 and current_element < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#             arr[j+1] = current_element
#     return arr


# s = [10, -4, -3, -2, -2, 4, 8, 2, 9, 5, 1]

# print (insertion_sort(s))

# # С БАРЬЕРАМИ 

# def insertion_barrier_sorting(arr):
#     arr = [0] + arr
#     for i in range (1, len(arr)):
#         arr[0] = arr[i]
#         j = i -1
#         while arr[0] < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = arr[0]
#     return arr[1:]

# s = [10, -4, -3, -2, -2, 4, 8, 2, 9, 5, 1]

# print (insertion_barrier_sorting(s))

# # БИНАРНЫМ

# def insertion_binary_sorting(arr):
#     for i in range (1, len(arr)):
#         current_element = arr[i]
#         lo = 0
#         hi = i
#         if lo == hi:
#             lo += 1
#         else:
#             while lo < hi:
#                 mid = (lo+hi) // 2
#                 if current_element < arr[mid] : 
#                     hi = mid
#                 else: lo = mid + 1
#         j = i 
#         while (j > lo and j > 0):
#             arr[j] = arr[j-1]
#             j -= 1
#         arr[lo] = current_element
#     return arr

# s = [4, 8, 2, 9, 5, 1]

# print (insertion_binary_sorting(s))


# ШЕЛЛ

def Shell_sort(arr):
    inc = len(arr) // 2
    while inc:
        for i, el in enumerate(arr):
            while i >= inc and arr[i-inc] > el:
                arr[i] = arr[i-inc]
                i -= inc
                arr[i] = el
        if inc == 2:
            inc = 1
        else:
            inc = int(inc*5.0 / 11)
    return (arr)

s = [4, 8, 2, 9, 5, 1]
print (Shell_sort(s))