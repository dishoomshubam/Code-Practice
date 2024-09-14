# def Double(arr):
#     x = []  # Initialize an empty list to store doubled values
#     for i in range(len(arr)):  # Loop through each element in the array
#         x.append(arr[i] * 2)  # Double the value and append to the new list
#     return x  # Return the new list


# arr = [2, 3, 2, 1, 2, 3]
# print(Double(arr))


# def CheckNum(arr):

#     num = []

#     seen = set()
#     duplicate = set()

#     for i in arr:

#         if i in seen:
#             duplicate.add(i)

#         else:
#             seen.add(i)

#     num = list(duplicate)

#     return num


# def CalculateNum(arr, num):
#     count = 0

#     index = num

#     for i in range(len(arr)):

#         if arr[i] == index:
#             count += 1

#     CheckNum(count)


# arr = [10, 5, 15, 10, 5, 15]
# print(CalculateNum(arr))


def CheckNum(arr):
    seen = set()  # Track seen numbers
    duplicate = set()  # Track duplicates

    for i in arr:
        if i in seen:
            duplicate.add(i)  # Add to duplicates if seen again
        else:
            seen.add(i)

    return list(duplicate)  # Return list of duplicates


def CalculateNum(arr, num):
    count = 0
    # Count occurrences of 'num' in 'arr'
    for i in range(len(arr)):
        if arr[i] == num:
            count += 1
    return count  # Return the count


arr = [10, 5, 15, 10, 5, 5]
duplicates = CheckNum(arr)  # Find duplicates

# Loop through the duplicates and count their occurrences
for num in duplicates:
    print(f"{num} occurs {CalculateNum(arr, num)} times")
