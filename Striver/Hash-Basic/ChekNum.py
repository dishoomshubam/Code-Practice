# chek a Num how many time in a array
# arr = [1,2,1,2,3,4,2]


def ListNum(arr, num):

    count = 0

    for i in range(len(arr)):
        if arr[i] == num:
            count = count + 1

    return count


arr = [1, 2, 3, 1, 2, 1, 4, 1]
num = 1
print(ListNum(arr, num))
