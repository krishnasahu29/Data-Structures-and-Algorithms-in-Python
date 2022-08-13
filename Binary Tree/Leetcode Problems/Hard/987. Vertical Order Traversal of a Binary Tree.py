# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        v_dist = 0
        h_dist = 0
        values = {}
        res = []

        self.verticalOrder(root, h_dist, v_dist, values)

        for x in sorted(values.keys()):
            column = [i[1] for i in sorted(values[x])]
            res.append(column)

        return res

    def verticalOrder(self, root, h_dist, v_dist, values):
        if not root:
            return

        if h_dist in values:
            values[h_dist].append((v_dist, root.val))
        else:
            values[h_dist] = [(v_dist, root.val)]

        self.verticalOrder(root.left, h_dist - 1, v_dist + 1, values)
        self.verticalOrder(root.right, h_dist + 1, v_dist + 1, values)


if __name__ == '__main__':
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)
    root.right = TreeNode(22)
    root.right.right = TreeNode(25)
    print(Solution().verticalTraversal(root))
