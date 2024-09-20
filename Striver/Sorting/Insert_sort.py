def Fun2(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

            arr[j + 1] = key

    return arr


arr = [3, 2, 1, 5, 6, 3, 2, 3, 45, 42, 1, 1, 3]
n = len(arr)
print(Fun2(arr, n))
