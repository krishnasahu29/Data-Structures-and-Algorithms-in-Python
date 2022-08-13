# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):

            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                temp = nums[i]
                nums[i] = nums[correct]
                nums[correct] = temp

            else:
                i += 1

        diss_nums = []

        for j in range(len(nums)):
            if nums[j] != j + 1:
                diss_nums.append(j + 1)

        return diss_nums


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
