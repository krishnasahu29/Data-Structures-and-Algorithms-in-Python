from typing import List


class Ternary:
    def search(self, arr: List[int], left: int, right: int, key: int):

        if right >= left:
            mid1 = left + (right - left) // 3
            mid2 = right - (right + left) // 3

            if key == arr[mid1]:
                return True

            elif key == arr[mid2]:
                return True

            elif key < arr[mid1]:
                return self.search(arr, left, mid1 - 1, key)

            elif key > arr[mid2]:
                return self.search(arr, mid2 + 1, right, key)

            else:
                return self.search(arr, mid1 + 1, mid2 - 1, key)

        return False


if __name__ == '__main__':
    arr = [7, 17, 19, 24, 51, 73, 96]
    key = 51
    left = 0
    right = len(arr) - 1
    print(Ternary().search(arr, left, right, key))
