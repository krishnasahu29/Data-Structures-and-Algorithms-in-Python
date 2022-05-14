from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0

        elif n == 1:
            return 1

        elif n == 2:
            return 1

        else:

            table: List[int] = [0] * (n + 1)
            table[1] = 1
            table[2] = 1

            for i in range(3, n + 1):
                table[i] = table[i - 1] + table[i - 2] + table[i - 3]

        return table[-1]


if __name__ == '__main__':
    print(Solution().tribonacci(37))
