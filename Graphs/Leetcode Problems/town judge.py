# https://leetcode.com/problems/find-the-town-judge/

from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        hash_table = defaultdict(list)
        ref = []
        for ch in trust:
            hash_table[ch[0]].append(ch[1])

        for i in range(1, N + 1):
            if i not in hash_table:
                ref.append(i)
        if len(ref) != 1:
            return -1
        n = ref[0]
        for j in hash_table:
            if n not in hash_table[j]:
                return -1
        return n


if __name__ == '__main__':
    print(Solution().findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))
