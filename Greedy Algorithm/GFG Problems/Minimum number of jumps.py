# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1?page=1&difficulty[]=1&category[]=Arrays&curated[]=1&sortBy=submissions

class Solution:
    def minJumps(self, arr, n):
        jumps = [0 for i in range(n)]

        if (n == 0) or (arr[0] == 0):
            return float('inf')

        jumps[0] = 0

        # Find the minimum number of
        # jumps to reach arr[i] from
        # arr[0] and assign this
        # value to jumps[i]
        for i in range(1, n):
            jumps[i] = float('inf')
            for j in range(i):
                if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                    jumps[i] = min(jumps[i], jumps[j] + 1)
                    break
        return jumps[n - 1]