from typing import List


def canSum(n: int, nums: List[int], memo=None) -> bool:

    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    if n == 0:
        return True

    if n < 0:
        return False

    for item in nums:
        rem = n - item
        if canSum(rem, nums, memo):
            memo[n] = True
            return True

    memo[n] = False
    return False


if __name__ == '__main__':
    print(canSum(7, [2, 3]))
    print(canSum(7, [5, 3, 4, 7]))
    print(canSum(7, [2, 4]))
    print(canSum(8, [2, 3, 5]))
    print(canSum(300, [7, 14]))
    print(canSum(300, [150, 100, 50]))
