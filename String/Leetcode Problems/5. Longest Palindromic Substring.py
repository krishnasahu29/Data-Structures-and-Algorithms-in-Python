# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len, lp = 0, ""
        for i in range(len(s)):
            # for odd length palindromic string
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    lp = s[left:right + 1]
                left -= 1
                right += 1
            # for even length palindromic string
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    lp = s[left:right + 1]
                left -= 1
                right += 1
        return lp


if __name__ == '__main__':
    print(Solution().longestPalindrome('babad'))
