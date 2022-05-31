# https://leetcode.com/problems/find-if-path-exists-in-graph/
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        visited = [False] * len(edges)

