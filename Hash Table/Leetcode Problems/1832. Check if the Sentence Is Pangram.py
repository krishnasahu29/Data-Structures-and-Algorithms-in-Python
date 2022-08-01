# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        hash_map = {}

        for ch in sentence:
            if ch not in hash_map.keys():
                hash_map[ch] = 0

            else:
                hash_map[ch] += 1

        if len(hash_map.keys()) == 26:
            return True

        return False


if __name__ == '__main__':
    print(Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
