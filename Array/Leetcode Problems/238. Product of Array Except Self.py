# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]

        left = 1
        right = 1

        for i in range(len(nums)):
            ans[i] *= left
            ans[-1 - i] *= right
            left *= nums[i]
            right *= nums[-1 - i]

        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf(nums=[1, 2, 3, 4]))
