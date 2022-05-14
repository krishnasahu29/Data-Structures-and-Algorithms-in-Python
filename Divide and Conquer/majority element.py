from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        print(c)
        return c.most_common()[0][0]

s = Solution()
print(s.majorityElement([6, 5, 5]))
