def FindString(arr, n):
    index = {}

    for i in range(n):
        if arr[i] in index:
            index[arr[i]] += 1
        else:
            index[arr[i]] = 1
    for x in index:
        alpha = "f"
        if x == alpha:
            print(x, index[x])


if __name__ == "__main__":

    arr = "kjhbdsahfj vbjan c;kjniuhepiuf dlnk nksancjlhsaiuyhdkandflknsa ;asknfijafnkjewnoe;k456789jnkej nfkiuhw78ey93nednsk saj"
    n = len(arr)
    FindString(arr, n)
