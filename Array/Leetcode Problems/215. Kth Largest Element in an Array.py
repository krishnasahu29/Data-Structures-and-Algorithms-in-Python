# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        s = tuple(nums_sorted)
        s = list(s)
        return s[-k]


if __name__ == '__main__':
    print(Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
