from typing import List


class Array:
    def sum_k(self, nums: List, k: int):
        i = 0
        j = len(nums) - 1

        while i < len(nums) - 1:
            if nums[i] + nums[j] == k:
                return True

            if j - i == 1:
                i += 1
                j = len(nums)

            j -= 1

        return False


if __name__ == '__main__':
    print(Array().sum_k([2, 6, 2, 5, 1], 3))
