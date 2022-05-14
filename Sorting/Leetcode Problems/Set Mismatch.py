from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = max(a for a, b in Counter(nums).items() if b == 2)
        nums.sort()
        nums.remove(d)
        for c, b in enumerate(nums, 1):
            if b != c:
                return [d, c]
        return [d, len(nums) + 1]


print(Solution().findErrorNums([2, 2]))
