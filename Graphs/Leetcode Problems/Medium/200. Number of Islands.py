# https://leetcode.com/problems/number-of-islands/
import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        v = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            v.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols)
                            and grid[r][c] == '1'
                            and (r, c) not in v):

                        q.append((r, c))
                        v.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in v:
                    bfs(r, c)
                    islands += 1

        return islands
