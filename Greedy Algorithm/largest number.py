from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.quickSort(nums, 0, len(nums) - 1)
        return str(int("".join(map(str, nums))))

    def quickSort(self, nums, left, right):
        if left >= right:
            return
        pos = self.partition(nums, left, right)
        self.quickSort(nums, left, pos - 1)
        self.quickSort(nums, pos + 1, right)

    def partition(self, nums, left, right):
        low = left
        while left < right:
            if self.compare(nums[left], nums[right]):
                nums[left], nums[low] = nums[low], nums[left]
                low += 1
            left += 1
        nums[low], nums[right] = nums[right], nums[low]
        return low

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

if __name__ == '__main__':
    print(Solution().largestNumber([3, 30, 34, 5, 9]))
