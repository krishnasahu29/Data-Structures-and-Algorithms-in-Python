# https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def minValue(root):

    if not root:
        return -1

    while root.left:
        root = root.left

    return root.data
