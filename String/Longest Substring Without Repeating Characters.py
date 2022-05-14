from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        i = 2

        freq = Counter(s)
        if len(freq) == 1:
            return 1

        while i < len(s) + 1:
            for j in range(len(s) - i + 1):
                freq = Counter(s[j:j + i])
                if len(freq) == len(s[j:j + i]) and len(freq) > max_len:
                    max_len = len(freq)

            i += 1

        return max_len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('pwwkew'))
