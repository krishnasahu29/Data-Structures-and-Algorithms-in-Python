from collections import defaultdict


class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowel = ["a", "e", "i", "o", "u"]
        hash_table = defaultdict(list)

        # for idx, v in enumerate(vowel):
        #     hash_table[idx].append(v)
        for i in range(len(vowel)):
            for j in range(i):
                pass
        # print(hash_table.values())

        return 0


if __name__ == '__main__':
    Solution().countVowelStrings(0)
