# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        hash_table = {}
        dfs = []
        stack = [root]
        res = []

        while stack:
            curr = stack.pop()
            dfs.append(curr.val)
            if curr.val in hash_table:
                hash_table[curr.val] += 1

            else:
                hash_table[curr.val] = 1

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        maxi = max(hash_table.values())

        for i in hash_table.keys():
            if hash_table[i] == maxi:
                res.append(i)

        return res
