# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
from collections import defaultdict
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            tmp, tmp2 = num - k, num + k
            if tmp in seen:
                counter += seen[tmp]
            if tmp2 in seen:
                counter += seen[tmp2]

            seen[num] += 1

        return counter


if __name__ == '__main__':
    print(Solution().countKDifference(nums=[1, 2, 2, 1], k=1))
