# https://leetcode.com/problems/find-if-path-exists-in-graph/
from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q = [source]
        visit.add(source)
        while q:
            node = q.pop(0)
            if node == destination:
                return True

            for nei in adj[node]:
                if nei not in visit:
                    q.append(nei)
                    visit.add(nei)
        return False
