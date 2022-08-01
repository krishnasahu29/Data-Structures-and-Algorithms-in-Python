# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.isSameTree(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    a1 = TreeNode(3)
    b1 = TreeNode(4)
    c1 = TreeNode(5)
    d1 = TreeNode(1)
    e1 = TreeNode(2)

    a2 = TreeNode(4)
    b2 = TreeNode(1)
    c2 = TreeNode(2)

    a1.left = b1
    a1.right = c1
    b1.left = d1
    b1.right = e1

    a2.left = b2
    a2.right = c2
    print(Solution().isSubtree(a1, a2))
