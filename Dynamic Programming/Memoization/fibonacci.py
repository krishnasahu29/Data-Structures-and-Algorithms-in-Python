# DP Approach

def fib(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]


if __name__ == '__main__':
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))
    print(fib(500))
