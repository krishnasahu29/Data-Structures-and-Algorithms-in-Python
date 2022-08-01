# https://leetcode.com/problems/contains-duplicate/

from typing import List
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = defaultdict()
        for num in nums:
            if num not in hash_table.keys():
                hash_table[num] = 1

            else:
                hash_table[num] += 1

        return hash_table


if __name__ == '__main__':
    print(Solution().containsDuplicate([1, 2, 3, 1]))
