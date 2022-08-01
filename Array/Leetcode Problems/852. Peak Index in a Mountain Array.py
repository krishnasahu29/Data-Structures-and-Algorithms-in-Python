# https://leetcode.com/problems/peak-index-in-a-mountain-array/
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """

        :param arr:
        :return:
        """
        l = 0
        r = len(arr) - 1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] > arr[m - 1] and arr[m] > arr[m + 1]:
                return m
            if arr[m] < arr[m + 1]:
                l = m + 1
            elif arr[m] < arr[m - 1]:
                r = m
        return -1


if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([0, 1, 4, 10, 2]))
