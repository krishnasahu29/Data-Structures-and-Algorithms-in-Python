# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

        # BFS
        # level = 0
        # q = deque([root])
        # if not root:
        #     return 0
        #
        # while q:
        #
        #     for i in range(len(q)):
        #         node = q.popleft()
        #
        #         if node.right:
        #             q.append(node.right)
        #
        #         if node.left:
        #             q.append(node.left)
        #
        #     level += 1
        #
        # return level

        # ITERATIVE DFS

        # if not root:
        #     return 0
        #
        # stack = [[root, 1]]
        # res = 1
        #
        # while stack:
        #     node, depth = stack.pop()
        #
        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
        #
        # return res
