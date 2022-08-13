# https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1

class Node:
    def __int__(self, x):
        self.data = x
        self.left = None
        self.right = None


class Solution:
    def getCount(self, root, low, high):
        res = []
        c = 0

        def inorder(root):
            if not root:
                return

            else:
                inorder(root.left)
                res.append(root.data)
                inorder(root.right)

        inorder(root)
        for i in res:
            if low <= i <= high:
                c += 1

        return c
