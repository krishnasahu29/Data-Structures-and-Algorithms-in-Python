# https://leetcode.com/problems/set-matrix-zeroes/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix[0])
        zero_cols = set()
        for r, row in enumerate(matrix):
            found_zero = False
            for c, el in enumerate(row):
                if el == 0:
                    zero_cols.add(c)
                    found_zero = True

            if found_zero:
                row[:] = [0] * m

        for r, row in enumerate(matrix):
            for c, el in enumerate(row):
                if c in zero_cols:
                    row[c] = 0

        return matrix


if __name__ == '__main__':
    print(Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
