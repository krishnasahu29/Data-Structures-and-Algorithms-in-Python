# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = 0, 0
        while i <= m and j <= n:
            if nums1[i] < nums2[j]:
                i += 1

            elif nums1[i] >= nums2[j]:
                nums1.append(nums2[j])
                j += 1

        # nums1 = nums1.extend(nums2)
        # nums1 = list(sorted(nums1))
        # for item in nums1:
        #     if item == 0:
        #         nums1.remove(item)


if __name__ == '__main__':
    print(Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
