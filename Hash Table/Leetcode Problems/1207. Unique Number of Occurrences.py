# https://leetcode.com/problems/unique-number-of-occurrences/
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_table = {}
        for num in arr:
            if num not in hash_table.keys():
                hash_table[num] = 0

            else:
                hash_table[num] += 1

        return len(hash_table.values()) == len(set(hash_table.values()))


if __name__ == '__main__':
    print(Solution().uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
