def bubble_sort_recursive(arr, n):

    if n == 1:
        return

    for i in range(n - 1):

        if arr[i] > arr[i + 1]:

            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    bubble_sort_recursive(arr, n - 1)


arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
Fun = bubble_sort_recursive(arr, n)
print(arr)


def merge(left, right):

    sorted_arr = []

    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            sorted_arr.append(left[i])

            i += 1

        else:

            sorted_arr.append(right[j])

            j += 1
dd
        while i < len(left):

            sorted_arr.append(left[i])

            i += 1

        while j < len(right):

            sorted_arr.append(right[j])

            j += 1

        return sorted_arr


def merge_sort(arr, n):

    if n > 1:

        mid = n // 2
        left = arr[mid:]
        right = arr[:mid]

        return merge(left, right)

    return arr


arr = [22, 34, 5, 12, 22, 11, 0]
n = len(arr)
Fun = merge_sort(arr, n)
print(Fun)
