def sum_natural(num: int) -> int:
    if num <= 1:
        return num

    return sum_natural(num - 1) + num


if __name__ == '__main__':
    print(sum_natural(5))
