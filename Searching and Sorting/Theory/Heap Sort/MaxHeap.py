from typing import List


class MaxHeap:

    def max_heapify(self, nums: List[int], n: int, i: int):
        pass

    def insert(self, nums: List, val: int):
        """
        :param nums: array
        :param val: value to be inserted in the array
        :return: None
        """
        nums.append(val)
        i = len(nums)
        while i > 1:
            parents = i // 2
            if nums[parents] < nums[i]:
                temp = nums[parents]
                nums[parents] = nums[i]
                nums[i] = temp

                i = parents

            else:
                return


if __name__ == '__main__':
    pass
