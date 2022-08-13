# https://www.geeksforgeeks.org/convert-normal-bst-balanced-bst/

class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def inorder(root, res):
    if not root:
        return

    else:
        inorder(root.left, res)
        res.append(root.data)
        inorder(root.right, res)


def inordertoBST(s, e, res) -> TreeNode:
    if s > e:
        return None
    mid = (s + e) // 2
    root = TreeNode(res[mid])
    root.left = inordertoBST(s, mid - 1, res)
    root.right = inordertoBST(mid + 1, e, res)
    return root


def binaryTreeToBst(root):
    # Write your code here.
    res = []
    inorder(root, res)

    return inordertoBST(0, len(res) - 1, res)
