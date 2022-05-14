# https://leetcode.com/problems/132-pattern/

from typing import List
from itertools import combinations


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        combs = combinations(nums, 3)

        for item in combs:
            if item[0] < item[2] < item[1]:
                return True

        return False


if __name__ == '__main__':
    print(Solution().find132pattern([-1, 3, 2, 0]))
