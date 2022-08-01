# https://leetcode.com/problems/roman-to-integer/
from collections import defaultdict


class Solution:

    def __init__(self):
        self.num = 0
        self.hash_table = defaultdict()

        self.hash_table['I'] = 1
        self.hash_table['V'] = 5
        self.hash_table['X'] = 10
        self.hash_table['L'] = 50
        self.hash_table['C'] = 100
        self.hash_table['D'] = 500
        self.hash_table['M'] = 1000

    def romanToInt(self, s: str) -> int:

        if s == '':
            return self.num

        if len(s) == 1:
            self.num += self.hash_table[s[0]]
            return self.romanToInt(s[1:])

        if s[0] == 'I' and s[1] == 'V' or s[0] == 'I' and s[1] == 'X':
            self.num += self.hash_table[s[1]] - self.hash_table[s[0]]
            return self.romanToInt(s[2:])

        if s[0] == 'X' and s[1] == 'L' or s[0] == 'X' and s[1] == 'C':
            self.num += self.hash_table[s[1]] - self.hash_table[s[0]]
            return self.romanToInt(s[2:])

        if s[0] == 'C' and s[1] == 'D' or s[0] == 'C' and s[1] == 'M':
            self.num += self.hash_table[s[1]] - self.hash_table[s[0]]
            return self.romanToInt(s[2:])

        else:
            self.num += self.hash_table[s[0]]
            return self.romanToInt(s[1:])


if __name__ == '__main__':
    print(Solution().romanToInt(s='MCMXCIV'))
