def palindrome(s: str):
    if len(s) == 0 or len(s) == 1:
        return True

    if s[0] == s[len(s) - 1]:
        return palindrome(s[1:len(s) - 1])

    return False


if __name__ == '__main__':

    print(palindrome('ma.am'))
