# https://leetcode.com/problems/rings-and-rods/

class Solution:
    def countPoints(self, rings: str) -> int:
        hash_func = {}
        c = 0

        for idx in range(0, len(rings) - 1, 2):
            if rings[idx + 1] in hash_func.keys():
                hash_func[rings[idx + 1]].append(rings[idx])

            else:
                hash_func[rings[idx + 1]] = list(rings[idx])

        # print(hash_func)
        for item in hash_func.values():
            if 'B' in item and 'R' in item and 'G' in item:
                c += 1

        return c


if __name__ == '__main__':
    print(Solution().countPoints("B0R0G0R9R0B0G0"))
