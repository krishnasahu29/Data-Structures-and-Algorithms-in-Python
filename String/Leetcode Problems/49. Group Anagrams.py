# https://leetcode.com/problems/group-anagrams/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()


if __name__ == '__main__':
    print(Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
