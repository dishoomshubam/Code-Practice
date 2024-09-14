# arr = [1,2,4,3,2,1]
# find how many time a 2 in this array


def FirstFunction(arr):
    count = 0
    num = 1
    num2 = 2
    for i in range(len(arr)):
        if arr[i] == num and num2:
            count += 1

    return count


arr = [1, 2, 4, 3, 2, 1]
print(FirstFunction(arr))


# find the String Char


def SecoundFunction(str):

    count = 0
    x = "a"

    for i in range(len(str)):

        if str[i] == x:
            count += 1

    return count


str = "asdfghasdfghasddfghj"
print(SecoundFunction(str))


def main():
    # Input number of elements
    n = int(input())

    # Input array elements
    arr = list(map(int, input().split()))

    # Precompute
    hash_map = [0] * 13
    for num in arr:
        hash_map[num] += 1

    # Input number of queries
    q = int(input())

    # Process each query
    for _ in range(q):
        number = int(input())
        # Fetching result for the query
        print(hash_map[number])


if __name__ == "__main__":
    main()
