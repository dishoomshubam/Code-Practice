def Number(n):
    divisor = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i)
    return divisor


n = 12
x = Number(n)
print(x)


import math


def OptimaceTime(N):
    esum = 0

    for i in range(1, N + 1):
        esum += i * (N // i)

    return esum


N = 5

Output = OptimaceTime(N)

print(Output)


def Number2(x):
    EmptyDivisor = []

    for i in range(1, x + 1):
        if x % i == 0:
            EmptyDivisor.append(i)

    return EmptyDivisor


x = 14
y = Number2(x)
print(y)


def TotalSumNumberDivision(n):
    total_sum = 0

    for i in range(1, n + 1):
        divisor_sum = 0

        for j in range(1, i + 1):

            if i % j == 0:
                divisor_sum += j

        total_sum += divisor_sum

    return total_sum


n = 4
x = TotalSumNumberDivision(n)
print(x)


def TotalDivaision(n):

    sum_total = 0

    for num in range(1, n + 1):

        divison_total = 0

        for num2 in range(1, num + 1):

            if num % num2 == 0:

                divison_total += num2

            sum_total += divison_total
    return sum_total


n = 4
x = TotalDivaision(n)
print(x)
