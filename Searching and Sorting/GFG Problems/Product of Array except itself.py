# https://www.geeksforgeeks.org/a-product-array-puzzle/
from typing import List


class Searching:
    def product_method1(self, arr: List[int], n: int) -> List[int]:
        if n == 1:
            print(0)
            return

        left = [0] * n
        right = [0] * n
        prod = [0] * n

        left[0] = 1
        right[n - 1] = 1

        for i in range(1, n):
            left[i] = arr[i - 1] * left[i - 1]

        for j in range(n - 2, -1, -1):
            right[j] = arr[j + 1] * right[j + 1]

        for i in range(n):
            prod[i] = left[i] * right[i]

        for i in range(n):
            print(prod[i], end=" ")

    def product_method2(self, arr: List[int], n: int) -> List[int]:
        prod = 1
        res = []

        for item in arr:
            prod *= item

        for item in arr:
            res.append(prod // item)

        print(res)

if __name__ == '__main__':
    arr = [10, 3, 5, 6, 2]
    n = len(arr)
    Searching().product_method2(arr, n)
