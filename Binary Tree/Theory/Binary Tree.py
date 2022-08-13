class TreeNode:
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def create(self) -> TreeNode:

        newNode = TreeNode()
        val = int(input("Enter value to be inserted ( -1 for no node) : "))
        if val == -1:
            return
        else:
            newNode.val = val
        print("Enter left child of {} ".format(val))
        newNode.left = self.create()
        print("Enter right child of {} ".format(val))
        newNode.right = self.create()
        return newNode

    def PreOrder(self, root: TreeNode) -> None:

        if root is None:
            return

        print(root.val, " ")
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def PostOrder(self, root: TreeNode) -> None:

        if root is None:
            return

        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.val, " ")

    def InOrder(self, root: TreeNode) -> None:

        if root is None:
            return

        self.InOrder(root.left)
        print(root.val, " ")
        self.InOrder(root.right)


if __name__ == '__main__':

    BT = BinaryTree()
    root = BT.create()
    print("Pre Order Traversal of the Binary Tree is")
    BT.PreOrder(root)
    print("Post Order Traversal of the Binary Tree is")
    BT.PostOrder(root)
    print("In Order Traversal of the Binary Tree is")
    BT.InOrder(root)
