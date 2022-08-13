from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        even: List[int] = []
        odd: List[int] = []

        for item in nums:
            if item % 2 == 0:
                even.append(item)
            else:
                odd.append(item)

        return even + odd


print(Solution().sortArrayByParity([1, 2, 3, 4]))
