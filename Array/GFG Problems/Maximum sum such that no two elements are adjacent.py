# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
from typing import List


class Array:
    def max_sum(self, arr: List[int], N):
        dp = [[0 for i in range(2)] for j in range(N)]
        if N == 1:
            return arr[0]

        dp[0][0] = 0
        dp[0][1] = arr[0]

        for i in range(1, N):
            dp[i][1] = dp[i - 1][0] + arr[i]
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])

        return max(dp[N - 1][0], dp[N - 1][1])


if __name__ == '__main__':
    arr = [5, 5, 10, 100, 10, 5]
    N = len(arr)
    print(Array().max_sum(arr, N))
