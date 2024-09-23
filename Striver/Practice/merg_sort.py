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


def sortMerge(arr):

    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = sortMerge(left)
        right = sortMerge(right)

        return merge(left, right)

    return arr


arr = [25, 45, 74, 85, 45, 6]


Func = sortMerge(arr)
print(Func)
