# https://leetcode.com/problems/word-pattern/
from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        hash_map = {}

        s_split = s.split()
        for i in range(len(s_split)):
            if pattern[i] not in hash_map.keys():
                l = [s_split[i]]
                hash_map[pattern[i]] = l

            else:
                hash_map[pattern[i]].append(s_split[i])

        for i in hash_map.keys():
            if len(set(hash_map[i])) != 1:
                return False

        return True


if __name__ == '__main__':
    print(Solution().wordPattern(pattern="abba", s="dog cat cat dog"))
