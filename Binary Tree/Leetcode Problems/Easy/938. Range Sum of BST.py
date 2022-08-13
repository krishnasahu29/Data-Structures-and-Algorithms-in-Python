# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        res = []
        s = 0

        if root is None:
            return

        # Create two stacks
        s1 = []
        s2 = []

        # Push root to first stack
        s1.append(root)

        # Run while first stack is not empty
        while s1:

            # Pop an item from s1 and
            # append it to s2
            node = s1.pop()
            s2.append(node)

            # Push left and right children of
            # removed item to s1
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

            # Print all elements of second stack
        while s2:
            node = s2.pop()
            res.append(node.val)

        for i in res:
            if low <= i <= high:
                s += i

        return s


if __name__ == '__main__':
    pass
