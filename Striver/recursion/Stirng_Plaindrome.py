def StringPalindrome(str, n):

    for i in range(n):
        print(str[i], end="")

    print()


def ReverString(str, n):

    ans = [0] * n

    for i in range(n - 1, -1, -1):
        ans[0 - i - 1] = str[i]

    StringPalindrome(ans, n)

    if str == "".join(ans):
        return True
    else:
        return False


if __name__ == "__main__":
    str = "ABCDCBA"
    n = len(str)
    if ReverString(str, n):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
