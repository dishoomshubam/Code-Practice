# Iterative Approach
def Factorial(N):

    # init 1
    result = 1

    # renge a N Number
    for i in range(1, N + 1):

        # divided per num

        result *= i
    return result


def main():
    N = 5
    print(Factorial(N))


if __name__ == "__main__":
    main()


# recursion Approch


def fact(X):

    if X == 0 or X == 1:
        return 1
    else:
        return X * fact(X - 1)


X = 22
print(fact(X))
