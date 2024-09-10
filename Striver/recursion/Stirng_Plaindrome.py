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


# To solve this problem, you need to convert the input string to lowercase,
# remove all non-alphanumeric characters, and then check if the resulting string is a palindrome.
# You can achieve this using Python string methods like lower() and isalnum(), and then compare the string to its reverse.
def isPalindrome(s: str) -> bool:
    # Convert the string to lowercase and filter only alphanumeric characters
    filtered_str = "".join(char.lower() for char in s if char.isalnum())

    # Check if the filtered string is equal to its reverse
    return filtered_str == filtered_str[::-1]


# Test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))  # Output: False
print(isPalindrome(" "))  # Output: True
