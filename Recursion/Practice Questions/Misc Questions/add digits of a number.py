def recursion(num: int) -> int:

    if num <= 0:
        return 0

    else:
        return num % 10 + recursion(int(num / 10))


if __name__ == '__main__':
    print(recursion(345))
