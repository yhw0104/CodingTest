input = "abcba"


def is_palindrome(string):
    # n = len(input)
    # for i in range(n):
    #     if string[i] != string[n - 1 - i]:
    #         return False
    # return True

    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1: -1])


print(is_palindrome(input))