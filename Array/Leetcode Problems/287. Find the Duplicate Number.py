# https://leetcode.com/problems/find-the-duplicate-number/
from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_table = defaultdict()

        for item in nums:
            if item in hash_table:
                hash_table[item] += 1

            else:
                hash_table[item] = 1

        # return hash_table
        for i in hash_table.keys():
            if hash_table[i] == 2:
                return i


if __name__ == '__main__':
    print(Solution().findDuplicate([1, 1, 2, 3, 4]))
