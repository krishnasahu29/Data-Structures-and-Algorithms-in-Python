# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        c = Counter(nums)
        freq = c.most_common(k)
        for i in freq:
            res.append(i[0])

        return res


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
