class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1:
            return True

        elif n < 1:
            return False

        else:
            return self.isPowerOfTwo(n / 2)


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(63356))
