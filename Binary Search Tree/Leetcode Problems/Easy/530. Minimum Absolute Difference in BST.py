# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(root):
            stack = [root]

            if not root:
                return []

            while len(stack) > 0:
                curr: TreeNode = stack.pop()
                res.append(curr.val)

                if curr.left:
                    stack.append(curr.left)

                if curr.right:
                    stack.append(curr.right)

            return res

        dfs(root)
        res.sort()
        for i in range(len(res) - 1):
            res[i] = res[i + 1] - res[i]

        return min(res)
