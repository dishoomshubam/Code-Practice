def Count(x):

    num = 0

    while x > 0:

        num = num + 1

        x = x // 10

    return num


x = 1234
print(Count(x))
