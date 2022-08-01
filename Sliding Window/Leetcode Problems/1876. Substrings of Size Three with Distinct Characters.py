# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i, j = 0, 3
        c = 0
        while j <= len(s):
            hash_count = {}
            for k in s[i:j]:
                if k not in hash_count.keys():
                    hash_count[k] = 1

            if len(hash_count) == 3:
                c += 1

            i += 1
            j += 1

        return c


if __name__ == '__main__':
    print(Solution().countGoodSubstrings("xyzzaz"))
