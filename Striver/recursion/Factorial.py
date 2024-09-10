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


def factorial_numbers(n):
    factorial_list = []
    fact = 1
    i = 1

    while fact <= n:
        factorial_list.append(fact)
        i += 1
        fact *= i

    return factorial_list


def factorial(n):

    fact_num = []
    facts = 1
    i = 1

    while facts <= n:

        fact_num.append(facts)

        i += 1

        facts *= i

    return fact_num


# Example usage:
n = 3
# print(factorial_numbers(n))
print(factorial(n))  # Output: [1, 2]

n = 10
print(factorial_numbers(n))  # Output: [1, 2, 6]
