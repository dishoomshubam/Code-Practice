def Fun2(arr, n):

    for i in range(n):
        Swap = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                Swap = True

        if not Swap:
            break

    return arr


arr = [3, 2, 1, 5, 6, 3, 2, 3, 45, 42, 1, 1, 3]
n = len(arr)
print(Fun2(arr, n))
