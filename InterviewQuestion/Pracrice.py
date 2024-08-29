def ReverseNum(x):

    num = 0

    while x > 0:

        id = x % 10

        num = (num * 10) + id

        x = x // 10

    return num


x = 21

print(ReverseNum(x))


# Recresion

count = 1


def func():

    global count

    if count == 3:
        return
    print(count)

    count += 1

    func()


def main():
    func()


if __name__ == "__main__":
    main()


def num(n):

    if n == 1:

        print(1, end=" ")

        return

    num(n - 1)

    print(n, end=" ")


n = 5

print(num(n))
