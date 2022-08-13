# https://practice.geeksforgeeks.org/problems/preorder-to-postorder4423/1

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def post_order(preorder, size) -> Node:
    inorder = sorted(preorder)

    def buildTree(preorder, inorder):
        if not preorder and not inorder:
            return None

        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

    return buildTree(preorder, inorder)
