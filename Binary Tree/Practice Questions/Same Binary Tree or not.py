class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sameTree(root1: TreeNode, root2: TreeNode) -> bool:
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val == root2.val and sameTree(root1.left, root2.left) and sameTree(root1.left, root2.right):
        return True


if __name__ == '__main__':
    a1 = TreeNode(1)
    b1 = TreeNode(2)
    c1 = TreeNode(3)

    a1.left = b1
    a1.right = c1

    a2 = TreeNode(1)
    b2 = TreeNode(2)
    c2 = TreeNode(3)

    a2.left = b2
    a2.right = c2

    print(sameTree(a1, a2))
