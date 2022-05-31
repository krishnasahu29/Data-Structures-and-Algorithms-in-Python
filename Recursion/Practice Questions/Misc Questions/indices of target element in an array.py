from typing import List
nums = []


def recursion(array: List[int], target: int, idx: int):
    if idx == len(array):
        return

    if array[idx] == target:
        nums.append(idx)

    recursion(array, target, idx + 1)


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 4, 5]
    recursion(arr, 4, 0)
    print(nums)
