class Solution:
    def reverseBits(self, n: int) -> int:

        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1

        return ret

print(Solution().reverseBits(0o0000010100101000001111010011100))
