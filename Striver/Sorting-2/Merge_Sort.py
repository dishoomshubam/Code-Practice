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

    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    while j < len(right):
        sorted_arr.append(right[j])

        j += 1

    return sorted_arr


def func(arr):

    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[mid:]
        right = arr[:mid]

        left = func(left)
        right = func(right)

        return merge(left, right)

    return arr


arr = [3, 2, 1, 4, 2, 5]
F = func(arr)
print(F)


def sort(left, right):

    sorted_arr = []

    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            sorted_arr.append(left[i])

            i += 1

        else:
            sorted_arr.append(right[j])

            j += 1

        while i < len(left):

            sorted_arr.append(left[i])

            i += 1

        while i < len(right):

            sorted_arr.append(right[j])

            j += 1

        return sorted_arr


def fun(arr):

    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[:mid]

        left = fun(left)
        right = fun(right)

        return sort(left, right)
    return arr


arr = [3, 2, 1, 4, 2, 5]
F1 = fun(arr)
print(F)
