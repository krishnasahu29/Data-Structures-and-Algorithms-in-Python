def recursion(num: int) -> int:
    if num == 0:
        return num

    else:
        return num + recursion(num - 2)


if __name__ == '__main__':
    print(recursion(6))
    print(recursion(10))
    