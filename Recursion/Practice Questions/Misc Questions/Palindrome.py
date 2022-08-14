def palindrome(s: str):
    if len(s) == 0 or len(s) == 1:
        return True

    elif s[0] == s[-1]:
        return palindrome(s[1:-1])

    else:
        return False


if __name__ == '__main__':

    print(palindrome('adam'))
