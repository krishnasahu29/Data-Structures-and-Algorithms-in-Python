from typing import List
from collections import defaultdict


def remove_duplicate(nums: List[int]) -> List[int]:
    hash_table = defaultdict()

    for idx, item in enumerate(nums):
        hash_table[idx] = item

    # print(hash_table.keys())
    # print((hash_table.values()))

    nums_dup = []

    for i in range(len(hash_table)):
        if hash_table[i] not in nums_dup:
            nums_dup.append(hash_table[i])

    return nums_dup


if __name__ == '__main__':
    print(remove_duplicate([1, 2, 3, 4, 1, 3, 8]))
