def SelctionShort(arr):

    # arr2 = []
    # # inncer loop
    # for i in range(len(arr)):
    #     print(arr[i], end="")

    #     for j in arr[i]:
    #         if j == min:
    #             arr2.append(j)
    #         else:
    #             False
    # return arr2

    # inncer loop
    for i in range(len(arr)):

        # Find the minimum element in the remaining unsorted array
        min_index = i

        # outer loops
        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [5, 6, 3, 4, 2, 1, 6, 7, 8]
print(SelctionShort(arr))
