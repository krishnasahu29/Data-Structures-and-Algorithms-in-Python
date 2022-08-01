# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        if not root:
            return 0

        while q:
            res_level = []

            for i in range(len(q)):
                node = q.popleft()

                if node.right:
                    q.append(node.right)
                    res_level.append(node.val)

                if node.left:
                    q.append(node.left)
                    res_level.append(node.val)

            res.append(res_level)

        return res


if __name__ == '__main__':
    pass
