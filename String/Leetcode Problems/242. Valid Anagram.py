# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_sort = sorted(s)
        t_sort = sorted(t)

        return s_sort == t_sort

if __name__ == '__main__':
    print(Solution().isAnagram(s="anagram", t="nagaram"))
