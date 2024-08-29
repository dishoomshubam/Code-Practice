# Print name N times using recursion without loops


def Program(N):

    if N <= 0:
        return

    print("Shubham", end=" ")

    # print a work on print a new line a  code
    print()

    Program(N - 1)


def main():

    N = int(input())

    Program(N)


if __name__ == "__main__":
    main()


# GFG Problem
# Print GFG n times without the loop.


# # Your Task:
# This is a function problem. You only need to complete the function printGfg() that takes N as parameter and prints N times GFG recursively. Don't print newline, it will be added by the driver code.


def ProgramGFG(N):

    if N <= 0:
        return

    print("GFG", end=" ")

    ProgramGFG(N - 1)


def main():

    N = int(input("Enter a Number :"))

    ProgramGFG(N)


if __name__ == "__main__":

    main()


# Print ( 1 - 4) N = 4 Output = 1, 2, 3, 4 without used loops


def ProgramNumber(N, i):

    if i > N:

        return

    print(i, end=", " if i < N else "")

    ProgramNumber(N, i + 1)


def main():

    i = 1
    N = int(input("Enter a n :"))

    ProgramNumber(N, i)


if __name__ == "__main__":

    main()

    # 1 , 2, 3, 4,


# Print ( 1 - 4) N = 4 Output = 3,2,1 without used loops


def ReverseProgram(N, I):

    if I < N:

        return

    print(N, end=" ," if I > N else "")

    ReverseProgram(I - 1, N)


def main():

    I = 1
    N = int(input("Enter a n :"))

    ProgramNumber(N, I)


if __name__ == "__main__":

    main()
