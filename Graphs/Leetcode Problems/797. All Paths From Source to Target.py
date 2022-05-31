# https://leetcode.com/problems/all-paths-from-source-to-target/
from collections import defaultdict
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        hash_table = defaultdict()

        for idx, i in enumerate(graph):
            hash_table[idx] = i

        pass


if __name__ == '__main__':
    Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []])
