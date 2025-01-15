def recursive_insertion_sort(arr, n, index=1):
    # Base case: if index reaches array size, sorting is complete
    if index == n:
        return

    # Store current element to be placed in correct position
    current = arr[index]
    j = index - 1

    # Move elements that are greater than current
    # to one position ahead of their current position
    while j >= 0 and arr[j] > current:
        arr[j + 1] = arr[j]
        j -= 1

    # Place current element in its correct position
    arr[j + 1] = current

    # Recursive call for next element
    recursive_insertion_sort(arr, n, index + 1)


# Helper function to make the interface simpler
def insertion_sort(arr):
    recursive_insertion_sort(arr, len(arr))
    return arr


# Test function to verify the implementation
def test_insertion_sort():
    # Test case 1
    arr1 = [13, 46, 24, 52, 20, 9]
    print("Test case 1:")
    print("Input:", arr1)
    print("Output:", insertion_sort(arr1.copy()))

    # Test case 2
    arr2 = [5, 4, 3, 2, 1]
    print("\nTest case 2:")
    print("Input:", arr2)
    print("Output:", insertion_sort(arr2.copy()))


# Run tests
if __name__ == "__main__":
    test_insertion_sort()
