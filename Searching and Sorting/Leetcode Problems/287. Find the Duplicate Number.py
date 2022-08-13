# https://leetcode.com/problems/find-the-duplicate-number/

from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):

            correct = nums[i] - 1

            if nums[i] != i + 1:
                if nums[i] != nums[correct]:
                    temp = nums[i]
                    nums[i] = nums[correct]
                    nums[correct] = temp

                else:
                    return nums[i]

            else:
                i += 1


if __name__ == '__main__':
    print(Solution().findDuplicate([1, 1, 2, 3, 4]))
