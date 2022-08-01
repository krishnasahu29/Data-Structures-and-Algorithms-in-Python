# https://leetcode.com/problems/next-greater-element-i/
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        container, stack = {}, []
        for num in nums2:
            while stack and num > stack[-1]:
                container[stack.pop()] = num
            stack.append(num)

        # print(container)
        return [container.get(num, -1) for num in nums1]


if __name__ == '__main__':
    print(Solution().nextGreaterElement(nums1=[1, 3, 5, 2, 4], nums2=[6, 5, 4, 3, 2, 1, 7]))
