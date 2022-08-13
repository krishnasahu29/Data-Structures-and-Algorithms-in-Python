# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = 0
        if not root.children or len(root.children) == 0:
            return 1

        for child in root.children:
            depth = max(depth, self.maxDepth(child))

        return depth + 1
