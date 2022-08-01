# https://leetcode.com/problems/permutations/
from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combs = permutations(nums)

        res = []
        for item in combs:
            res.append(list(item))

        return res


if __name__ == '__main__':
    print(Solution().permute([0, 1]))
