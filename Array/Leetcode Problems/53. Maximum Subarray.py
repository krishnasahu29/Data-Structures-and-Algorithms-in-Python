# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -99999
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]
            if curSum > maxSum:
                maxSum = curSum

            if curSum < 0:
                curSum = 0

        return maxSum
