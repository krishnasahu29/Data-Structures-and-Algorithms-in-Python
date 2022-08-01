# https://www.geeksforgeeks.org/chocolate-distribution-problem/
from collections import defaultdict
from typing import List


class Array:
    def chocolates(self, packets: List[int], students: int):
        B, C = [], defaultdict(list)
        for x in packets:
            C[x].append(x)

        print(C)

        for k in range(min(C), max(C) + 1):
            B.extend(C[k])

        print(B)

        i = 0
        j = students - 1
        diff = 9999
        while j < len(B):
            if B[j] - B[i] < diff:
                diff = B[j] - B[i]

            i += 1
            j += 1

        return diff


if __name__ == '__main__':
    print(Array().chocolates(packets=[3, 4, 1, 9, 56, 7, 9, 12], students=5))
