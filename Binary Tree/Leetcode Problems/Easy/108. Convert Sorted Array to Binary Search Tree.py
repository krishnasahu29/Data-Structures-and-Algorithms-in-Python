# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None

            # find middle index
        mid = (len(arr)) // 2

        # make the middle element the root
        root = TreeNode(arr[mid])

        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sortedArrayToBST(arr[:mid])

        # right subtree of root has all
        # values >arr[mid]
        root.right = self.sortedArrayToBST(arr[mid + 1:])
        return root

    # A utility function to print the preorder
    # traversal of the BST
    def preOrder(node):
        if not node:
            return

