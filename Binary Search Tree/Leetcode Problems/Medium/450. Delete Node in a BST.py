# https://leetcode.com/problems/delete-node-in-a-bst/

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                temp = root.right
                root = None
                return temp

            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.minValue(root.right)
            root.val = temp.val

            root.right = self.deleteNode(root.right, temp.val)

        return root

    def minValue(self, node: TreeNode):
        curr = node
        while curr.left:
            curr = curr.left

        return curr
