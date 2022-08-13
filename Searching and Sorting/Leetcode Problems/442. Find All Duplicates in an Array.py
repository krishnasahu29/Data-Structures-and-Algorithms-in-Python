# https://leetcode.com/problems/find-all-duplicates-in-an-array/
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):

            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                temp = nums[i]
                nums[i] = nums[correct]
                nums[correct] = temp

            else:
                i += 1

        nums_dupl = []

        for i in range(len(nums)):
            if nums[i] != i + 1:
                nums_dupl.append(i + 1)

        return nums_dupl
