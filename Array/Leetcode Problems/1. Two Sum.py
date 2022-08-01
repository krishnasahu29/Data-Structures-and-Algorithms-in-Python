# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], idx]

            prevMap[num] = idx
        return


if __name__ == '__main__':
    print(Solution().twoSum([3, 2, 4], 6))
