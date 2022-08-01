# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        for i in range(n - 1):
            prices[i] = prices[i + 1] - prices[i]

        print(prices)

        # kadane Algo
        MaxSum = 0
        Sum = 0
        for i in range(n - 1):
            Sum += prices[i]
            MaxSum = max(MaxSum, Sum)

            if Sum < 0:
                Sum = 0

        if MaxSum <= 0:
            return 0

        return MaxSum


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
