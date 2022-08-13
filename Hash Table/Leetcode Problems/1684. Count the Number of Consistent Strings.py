from collections import defaultdict
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # hash_table = defaultdict(list)
        # for idx, ch in enumerate(allowed):
        #     hash_table[idx].append(ch)
        res1 = ''.join(format(ord(i), '08b') for i in "ab")
        res2 = ''.join(format(ord(i), '08b') for i in "baa")
        print(res1 & res2)

        return 0


if __name__ == '__main__':
    Solution().countConsistentStrings(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"])
