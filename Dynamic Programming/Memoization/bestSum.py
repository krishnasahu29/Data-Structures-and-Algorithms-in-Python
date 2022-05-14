from typing import List


def bestSum(targetSum: int, bestSumlist: List[int], memo=None) -> List[int]:

    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None

    shortest_comb = None

    for i in bestSumlist:
        remainder = targetSum - i
        remainder_combination = bestSum(remainder, bestSumlist, memo)
        if remainder_combination is not None:
            combination = remainder_combination + [i]
            if shortest_comb is None or len(shortest_comb) > len(combination):
                shortest_comb = combination

    memo[targetSum] = shortest_comb
    return shortest_comb


if __name__ == '__main__':
    print(bestSum(7, [7, 3, 4, 5]))
    print(bestSum(8, [2, 3, 5]))
    print(bestSum(8, [1, 4, 5]))
    print(bestSum(100, [1, 2, 5, 25]))
