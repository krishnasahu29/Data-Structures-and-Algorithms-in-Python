def binary(num: int, result: str) -> str:
    if num == 0:
        return result

    result = str(num % 2) + result
    return binary(num // 2, result)


if __name__ == '__main__':
    print(binary(20, ''))
