# https://leetcode.com/problems/integer-to-roman/
from collections import defaultdict


class Solution:
    def intToRoman(self, num: int) -> str:

        hash_table = defaultdict()
        hash_table['I'] = 1
        hash_table['V'] = 5
        hash_table['X'] = 10
        hash_table['L'] = 50
        hash_table['C'] = 100
        hash_table['D'] = 500
        hash_table['M'] = 1000
