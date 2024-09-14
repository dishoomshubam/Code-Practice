# def Freq(arr, n):

#     value = {}

#     for i in range(n):
#         if arr[i] in value:
#             value[arr[i]] += 1

#         else:
#             value[arr[i]] = 1

#     for j in value:
#         print(j, value[j])


# if __name__ == "__main__":

#     arr = [10, 4, 10, 4, 5]
#     n = len(arr)
#     Freq(arr, n)


def Freq(arr, n):

    value = []

    for i in range(len(arr)):
        print(i)


if __name__ == "__main__":

    arr = [2, 4, 1, 4, 2]
    n = int(input())

    Freq(arr, n)
