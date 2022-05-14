from typing import List


def howSum(targetSum: int, nums: List[int], memo=None) -> List[int]:
    if memo is None:
        memo = {}
        
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for item in nums:
        rem = targetSum - item
        remResult = howSum(rem, nums, memo)
        if remResult is not None:
            memo[targetSum] = remResult + [item]
            return memo[targetSum]

    memo[targetSum] = None
    return None


if __name__ == '__main__':
    print(howSum(7, [2, 3]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(7, [2, 4]))
    print(howSum(8, [3, 5, 2]))
    print(howSum(300, [30, 20]))
