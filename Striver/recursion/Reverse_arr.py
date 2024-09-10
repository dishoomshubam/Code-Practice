# function to print array
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, n):
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[n - i - 1] = arr[i]
    printArray(ans, n)


# Driver Code
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)


def SameArray(arr, n):

    for i in range(n):

        print(arr[i], end=" ")

    print()


def ReverArray(arr, n):

    x = [0] * n

    for i in range(n, -1, -1, -1):
        x[n - i - 1] = arr[i]

    SameArray(arr, n)


def main():

    arr = [1, 2, 3, 4, 5]

    n = len(arr)

    ReverArray(arr, n)


if __name__ == "__main__":
    main()
