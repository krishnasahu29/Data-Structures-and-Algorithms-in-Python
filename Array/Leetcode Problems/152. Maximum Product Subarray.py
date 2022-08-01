# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = 1
        r = -99999

        for i in range(len(nums)):
            p *= nums[i]
            r = max(r, p)

            if p == 0:
                p = 1

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            p *= nums[i]
            r = max(r, p)

            if p == 0:
                p = 1

        return r


if __name__ == '__main__':
    print(Solution().maxProduct([2, 3, -2, 4]))
