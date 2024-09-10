# First Approch
def String(str, n):

    for i in range(n):
        print(str[i], end=" ")

    print()


def ReverString(str, n):

    ans = [0] * n

    for i in range(n - 1, -1, -1):

        ans[n - i - 1] = str[i]

    String(ans, n)


if __name__ == "__main__":
    str = "shubham"
    n = len(str)

    ReverString(str, n)


# 2 Approch  while loops


def SecoundAproch(arr, n):

    for i in range(n):
        print(arr[i], end=" ")

    print()


def Secoundrevers(arr, n):

    p1 = 0

    p2 = n - 1

    while p1 < p2:

        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1

    SecoundAproch(arr, n)


if __name__ == "__main__":

    arr = [12, 32, 12, 34, 11]  # o/p : 11 34 12 32 12
    n = len(arr)
    Secoundrevers(arr, n)


# Recursive method  if else


def RechArray(arr, n):

    for i in range(n):
        print(arr[i], end=" ")

    print()


def RechReverse(arr, start, end):

    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        RechReverse(arr, start + 1, end - 1)

    # Driver Code


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    RechReverse(arr, 0, n - 1)
    RechArray(arr, n)


# Using library function (New Approach)


def reverserArrray(arr, n):

    for i in range(n):
        print(arr[i], end=" ")

    print


def reverusedLibrary(arr, n):

    arr.reverse()


if __name__ == "__main__":
    arr = [
        4,
        1,
        2,
        3,
        21,
        2,
        34,
    ]
    n = len(arr)
    reverusedLibrary(arr, n)
    reverserArrray(arr, n)
