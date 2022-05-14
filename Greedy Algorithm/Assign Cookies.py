from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = sorted(g), sorted(s)
        i, j, c = 0, 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                j += 1
                c += 1

            else:
                j += 1

        return c


if __name__ == '__main__':
    print(Solution().findContentChildren(g=[1, 2], s=[1, 2, 3]))
