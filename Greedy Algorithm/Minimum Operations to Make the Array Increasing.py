from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        c = 0
        n = len(nums) - 1

        i = n

        while i >= 0:
            while nums[i] <= nums[i - 1]:
                nums[i] += 1

            if i <= (n - 1) and nums[i] >= nums[i+1]:
                i += 1

            i -= 1
            c += 1

        return c


print(Solution().minOperations(nums=[1, 5, 2, 4, 1]))
