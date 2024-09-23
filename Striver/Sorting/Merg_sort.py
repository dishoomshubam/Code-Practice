def merge(left_half, right_half):

    sorted_arr = []

    i = j = 0
    # Compare and merge elements from both halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1

        else:
            sorted_arr.append(right_half[j])
            j += 1

    # Append remaining elements from left_half (if any)
    while i < len(left_half):

        sorted_arr.append(left_half[i])
        i += 1
    # Append remaining elements from right_half (if any)
    while j < len(right_half):
        sorted_arr.append(right_half[j])
        j += 1

    return sorted_arr


def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point and divide the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves

        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        # Merge the sorted halves
        return merge(left_half, right_half)

    return arr


arr = [3, 2, 1, 5, 6, 3, 2, 3, 45, 42, 1, 1, 3]

sorted_arr = merge_sort(arr)
print(sorted_arr)
