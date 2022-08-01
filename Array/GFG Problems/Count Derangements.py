def countDer(n: int) -> int:
    if n == 1 or n == 2:
        return n - 1

    a = 0
    b = 1

    for i in range(3, n + 1):
        cur = (i - 1) * (a + b)
        a = b
        b = cur

    return b


if __name__ == '__main__':
    n = 4
    print("The Count of Derangements is", countDer(n))
