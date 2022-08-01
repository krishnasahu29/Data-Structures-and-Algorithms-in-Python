# https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

from itertools import combinations
from typing import List


class Array:
    def triplets(self, arr: List[int], s: int):
        c = 0
        combs = combinations(arr, 3)
        for item in combs:
            if sum(item) < s:
                c += 1

        return c


if __name__ == '__main__':
    print(Array().triplets([5, 1, 3, 4, 7], 12))
