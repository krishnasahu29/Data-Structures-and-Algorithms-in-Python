# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = right = 0
        q = deque()  # contain indices

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # remove left val from window
            if left > q[0]:
                q.popleft()

            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1

            right += 1

        return res


if __name__ == '__main__':
    pass
