# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
from typing import List


class Duplicates:

    def find_dups(self, nums: List[int], n: int):
        i = 0
        while i < len(nums):

            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                temp = nums[i]
                nums[i] = nums[correct]
                nums[correct] = temp

            else:
                i += 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])

        return nums
