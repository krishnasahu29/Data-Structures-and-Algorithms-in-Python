# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):

            correct = nums[i]
            if nums[i] < len(nums) and nums[i] != nums[correct]:
                temp = nums[i]
                nums[i] = nums[correct]
                nums[correct] = temp

            else:
                i += 1

        for j in range(len(nums)):
            if j != nums[j]:
                return j

        return len(nums)
    