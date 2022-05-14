from itertools import combinations
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        out: List[int] = [i for i in list(combinations(nums, r=3))]
        return list(set(i for i in out if sum(i) == 0))

        # for i in range(len(nums) - 2):
        #     if sum(nums[i:i+3]) == 0:
        #         out.append(nums[i:i+3])
        #     print(nums[i:i+3])

        # return out

print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
