# https://leetcode.com/problems/happy-number/

class Solution:

    def __init__(self):
        self.hashSet = set()

    def isHappy(self, n: int) -> bool:

        if self.getSum(n) == 1:
            return True

        if self.getSum(n) in self.hashSet:
            return False

        else:
            self.hashSet.add(self.getSum(n))
            return self.isHappy(self.getSum(n))

    def getSum(self, n):
        s = 0
        for digit in str(n):
            s += int(digit) ** 2
        return s


if __name__ == '__main__':
    print(Solution().isHappy(1111111))
