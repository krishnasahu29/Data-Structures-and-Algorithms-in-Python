# https://leetcode.com/problems/climbing-stairs/
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:

        # O(N) SPACE COMPLEXITY
        # n = n + 1
        #
        # table: List[int] = [0] * (n + 1)
        # table[1] = 1
        #
        # for i in range(2, n + 1):
        #     table[i] = table[i - 1] + table[i - 2]
        # return table[n]

        # O(1) SPACE COMPLEXITY
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


if __name__ == '__main__':
    print(Solution().climbStairs(2))
