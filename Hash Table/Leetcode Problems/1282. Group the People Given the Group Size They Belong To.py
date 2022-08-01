# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hash_map = defaultdict()

        for idx, i in enumerate(groupSizes):
            pass
