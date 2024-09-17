# arr = [1,2,3,4,5]
# ind = 2
# output arr = [3,2,1,5,4]


def ReversNumber(arr, n):

    for i in range(n):
        print(arr[i], end=" ")

    print()


def reverNumber(arr, n):
    num = [0] * n

    for x in range(n - 1, -1, -1):

        num[n - x - 1] = arr[x]

    ReversNumber(num, x)


arr = [1, 2, 3, 4, 5]
ind = 2
n = len(arr)
print(reverNumber(arr, n))
