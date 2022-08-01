# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# RECURSIVE
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         """
#         :type root: Node
#         :rtype: List[int]
#         """
#         res = []
#         if root is None:
#             return res
#
#         def recursion(root, res):
#             for child in root.children:
#                 recursion(child, res)
#             res.append(root.val)
#
#         recursion(root, res)
#         return res

# ITERATIVE
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None:
            return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)

        return res[::-1]

if __name__ == '__main__':
    pass
