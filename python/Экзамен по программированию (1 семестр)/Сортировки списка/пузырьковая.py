def bubble_sort(arr):
    arr_length = len(arr)
    for i in range (arr_length-1):
        for j in range (arr_length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

s = [4, 8, 2, 9, 5, 1]
print (bubble_sort(s))


# # Пузырьквая с флагом

# def bubble_sort_flag(arr):
#     arr_length = len(arr)
#     for i in range (arr_length-1):
#         flag = True
#         for j in range (arr_length - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1], arr[j]
#                 flag = False
#         if flag:
#             break

#     return arr

# s = [-4, -3, -2, -1, 4, 8, 2, 9, 5, 1]

# print (bubble_sort_flag(s))

# Шейкер 

# def shaker_sort(arr):
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         r_new = left
#         for i in range (left, right):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 r_new = i
#         right = r_new
#         l_new = right
#         for i in range (right - 1, left - 1, -1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 l_new = i
#         left = l_new

#     return arr

# s = [10, -4, -3, -2, -1, 4, 8, 2, 9, 5, 1]

# print (shaker_sort(s))