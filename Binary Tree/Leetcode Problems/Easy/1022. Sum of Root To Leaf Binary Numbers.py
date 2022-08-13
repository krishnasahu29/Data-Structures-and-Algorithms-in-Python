# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def preorder(node: TreeNode, binary):
            if not node:
                return

            preorder(node.left, binary + str(node.val))
            preorder(node.right, binary + str(node.val))

            if not node.left and not node.right:
                self.total += int(binary + str(node.val), 2)

        preorder(root, "")

        return self.total


if __name__ == '__main__':
    a: TreeNode = TreeNode(1)
    b: TreeNode = TreeNode(0)
    c: TreeNode = TreeNode(1)
    d: TreeNode = TreeNode(0)
    e: TreeNode = TreeNode(1)
    f: TreeNode = TreeNode(0)
    g: TreeNode = TreeNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    print(Solution().sumRootToLeaf(a))
