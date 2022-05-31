from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str, memo=None) -> List[int]:

        if memo is None:
            memo = {}

        if n in memo:
            return memo[i]


if __name__ == '__main__':
    print(Solution().diffWaysToCompute("2-1-1"))
