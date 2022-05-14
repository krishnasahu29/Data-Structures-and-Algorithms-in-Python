from typing import List


def fib(n: int) -> int:

    table: List[int] = [0] * (n+1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]

if __name__ == '__main__':
    print(fib(7))
    print(fib(12))
    print(fib(20))
    print(fib(50))
    print(fib(500))
