from typing import List


class Recursion:
    def list_sum(self, num_List: List) -> int:
        if len(num_List) == 1:
            return num_List[0]
        else:
            return num_List[0] + self.list_sum(num_List[1:])


if __name__ == '__main__':
    print(Recursion().list_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
