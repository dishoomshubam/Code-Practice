def Fun(arr, n):
    if n > 1:
        # Find the middle point and divide the array into two halves
        mid = n // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively call merge_sort on both halves
        Fun(left_half, len(left_half))
        Fun(right_half, len(right_half))

        # Merging the sorted halves
        i = j = k = 0

        # Copy data to temporary arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any elements were left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any elements were left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [3, 2, 1, 5, 6, 3, 2, 3, 45, 42, 1, 1, 3]
n = len(arr)
Fun(arr, n)
print(arr)
