from typing import List


class CyclicSort:
    def sort(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):

            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                temp = nums[i]
                nums[i] = nums[correct]
                nums[correct] = temp

            else:
                i += 1

        return nums


if __name__ == '__main__':
    print(CyclicSort().sort([3, 2, 1, 4, 5]))
