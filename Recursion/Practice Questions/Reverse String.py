from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return reversed(s)


if __name__ == '__main__':
    print(Solution().reverseString(["h", "e", "l", "l", "o"]))
