# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def parser(root, lt):
            if not root:
                return
            parser(root.left, lt)
            lt.append(root.val)
            parser(root.right, lt)

        lt = list()
        parser(root, lt)
        head = None
        output = None
        for ele in lt:
            if not head:
                head = TreeNode(ele)
                output = head
            elif ele:
                head.right = TreeNode(ele)
                head = head.right
        return output


if __name__ == '__main__':

    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(8)
    i = TreeNode(9)

    e.left = c
    e.right = f
    c.left = b
    c.right = d
    b.left = a
    f.right = h
    h.right = i

    Solution().increasingBST(e)
