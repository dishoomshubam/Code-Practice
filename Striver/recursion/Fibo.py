# def Fib(n):

#     if n == 0:
#         return 0

#     elif n == 1:
#         return 1

#     else:
#         Fib(n - 1) + Fib(n - 2)


# def series(n):
#     for i in range(n):
#         print(Fib(i), end=" ")


# series(11)


#


#
# def fibonacci(n):
#     # Base cases
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         # Recursive case
#         return fibonacci(n - 1) + fibonacci(n - 2)


# # Generate Fibonacci series for the first 'n' numbers
# def fibonacci_series(n):
#     for i in range(n):
#         print(fibonacci(i), end=" ")


# # Example: Print the first 10 Fibonacci numbers
# fibonacci_series(10)


def fibonanchiseries(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibonanchiseries(n - 1) + fibonanchiseries(n - 2)

    # a, b = 0, 1
    # for _ in range(2, n + 1):
    #     a, b = b, a + b
    # return b


print(fibonanchiseries(4))
