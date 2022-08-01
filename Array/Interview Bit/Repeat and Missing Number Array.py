# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, nums):
        i = 0
        nums = list(nums)
        while i < len(nums):

            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]

            else:
                i += 1

        for idx, item in enumerate(nums):
            if item - 1 != idx:
                return [item, idx + 1]


if __name__ == '__main__':
    print(Solution().repeatedNumber((3, 1, 2, 5, 3)))
