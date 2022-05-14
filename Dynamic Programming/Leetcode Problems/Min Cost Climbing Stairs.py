from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f: List[int] = [0] * (len(cost))

        if not cost:
            return 0

        f[0] = cost[0]

        if len(cost) >= 2:
            f[1] = cost[1]
        else:
            return f[-1]

        for i in range(2, len(cost)):
            f[i] = cost[i] + min(f[i-1], f[i-2])

        print(f)
        return min(f[-1], f[-2])


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs(cost=[10]))
