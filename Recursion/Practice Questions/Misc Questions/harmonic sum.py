def recursion(num):
    if num == 1:
        return 1

    else:
        return 1 / num + recursion(num - 1)


if __name__ == '__main__':
    print(recursion(7))
    print(recursion(4))
    