from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        table: List[int] = []

        table[0] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            pass
