# https://leetcode.com/problems/find-peak-element/
from typing import List


class Solution:
    def __init__(self):
        self.c = 0

    def findPeakElement(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return self.c

        if arr[0] < arr[1]:
            self.c += 1
            return self.findPeakElement(arr[1:])

        else:
            return self.c


if __name__ == '__main__':
    print(Solution().findPeakElement([0, 10, 2, 1]))
