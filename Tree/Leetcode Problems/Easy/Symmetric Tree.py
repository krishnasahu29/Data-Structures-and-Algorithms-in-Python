# Definition for a binary tree node.
from typing import Optional, List

res = []

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pass

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper_post(root, res)
        return res

    def helper_post(self, root, res):

        if root:
            self.helper_post(root.left, res)
            self.helper_post(root.right, res)
            res.append(root.val)
