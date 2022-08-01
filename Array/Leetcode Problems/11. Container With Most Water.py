# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lptr, rptr = 0, len(height) - 1
        area = 0
        while lptr <= rptr:
            area = max(area, min(height[lptr], height[rptr]) * (rptr - lptr))
            if height[lptr] <= height[rptr]:
                lptr += 1
            else:
                rptr -= 1
        return area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
