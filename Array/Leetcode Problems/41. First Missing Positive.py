# https://leetcode.com/problems/first-missing-positive/
from typing import List
from collections import defaultdict


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):

            correct = nums[i] - 1
            if 0 < nums[i] <= len(nums) and nums[i] != nums[correct]:
                temp = nums[i]
                nums[i] = nums[correct]
                nums[correct] = temp

            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([-1, 0, 1, 2]))
