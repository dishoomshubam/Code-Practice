# def countFrequencies(arr, n, p):
#     # Step 1: Traverse the array and increase the value at the corresponding index
#     for i in range(len(arr)):
#         if arr[i] <= n:  # Only count numbers <= n
#             # Use modulus technique to store frequency count within the same array
#             index = arr[i] - 1  # Convert 1-based index to 0-based
#             arr[index] = arr[index] + p  # Increment by 'p' to encode count

#     # Step 2: Extract frequencies by dividing by 'p'
#     for i in range(n):
#         arr[i] = arr[i] // p  # Frequency is encoded as original_val + p*frequency

#     return arr[:n]  # Return only the first n elements as required


# # Test Case 1
# arr = [2, 3, 2, 3, 5]
# n = 5
# p = 5
# print(countFrequencies(arr, n, p))  # Output: [0, 2, 2, 0, 1]

# # Test Case 2
# arr = [3, 3, 3, 3]
# n = 4
# p = 3
# print(countFrequencies(arr, n, p))  # Output: [0, 0, 4, 0]

# # Test Case 3
# arr = [8, 9]
# n = 2
# p = 9
# print(countFrequencies(arr, n, p))  # Output: [0, 0]


def countFreq(arr, n):

    visited = [False] * n

    for i in range(n):
        if visited[i] == True:
            continue
        count = 1

        for j in range(i + 1, n):
            if arr[i] == arr[j]:

                visited[j] = True

            count += 1

        print(arr[i], count)


if __name__ == "__main__":
    arr = [1, 2, 3, 2, 1, 3, 4, 2, 1, 3]
    n = len(arr)
    countFreq(arr, n)


# using Map


def Frequency(arr, n):
    mp = {}

    for i in range(n):

        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    for x in mp:

        print(x, "-", mp[x])


if __name__ == "__main__":

    arr = [10, 4, 10, 4, 5]
    n = len(arr)
    Frequency(arr, n)


def Freq(arr, n):

    pair = {}

    for i in range(n):

        if arr[i] in pair:

            pair[arr[i]] += 1
        else:
            pair[arr[i]] = 1

    for x in pair:

        print(x, pair[x])


if __name__ == "__main__":

    arr = [10, 4, 10, 4, 5]
    n = len(arr)
    Freq(arr, n)
