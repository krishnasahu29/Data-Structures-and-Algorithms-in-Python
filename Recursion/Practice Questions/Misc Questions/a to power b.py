def recursion(a: int, b: int) -> int:
    if b == 0:
        return 1

    else:
        return a * recursion(a, b - 1)


if __name__ == '__main__':

    print(recursion(3, 4))
    print(recursion(5, 3))
    