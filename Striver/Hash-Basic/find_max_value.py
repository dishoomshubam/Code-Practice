def Max_value(arr):

    from collections import Counter

    frquently = Counter(arr)

    max_freq = max(frquently.values())
    min_freq = min(frquently.values())

    highest_freq = [
        num for num, frquently in frquently.items() if frquently == max_freq
    ]
    lowest_freq = [num for num, frquently in frquently.items() if frquently == min_freq]

    highest_freq = highest_freq[0]
    lowest_freq = lowest_freq[0]

    return highest_freq, lowest_freq


arr = [10, 5, 10, 15, 10, 5]
print(Max_value(arr))
