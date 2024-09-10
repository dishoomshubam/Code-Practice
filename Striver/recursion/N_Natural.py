def Natural(N):

    # total sum intiliaze 0
    tsum = 0

    # for loop to to used a renge 1 to N

    for i in range(1, N + 1):

        #  addition a number
        tsum += i

        # return the value
    return tsum


def main():
    N = 5
    print(Natural(N))


if __name__ == "__main__":
    main()
