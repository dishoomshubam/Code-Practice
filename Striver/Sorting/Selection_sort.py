def fun1(arr, i):

    min_index = i

    for j in range(i + 1, len(arr)):

        if arr[j] < arr[min_index]:
            min_index = j

    return min_index


def Fun2(arr, n):

    for i in range(n):

        index = fun1(arr, i)

        arr[i], arr[index] = arr[index], arr[i]


arr = [3, 2, 1, 5, 6, 3, 2, 3, 45, 42, 1, 1, 3]
n = len(arr)
print(Fun2(arr, n))
