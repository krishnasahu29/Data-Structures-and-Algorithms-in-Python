class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class PrintAllNodes:

    def insert_node(self, root: TreeNode, val):

        if root is None:
            return TreeNode(val)

        else:
            if val == root.data:
                return root

            elif val < root.left:
                root.left = self.insert_node(root.left, val)

            else:
                root.right = self.insert_node(root.right, val)

        return root

    def printNodes(self, root: TreeNode):
        if root is None:
            return

        if root.left is None and root.right is None:
            print(root.data, end=", ")
            return

        if root.left is not None:
            self.printNodes(root.left)

        if root.right is not None:
            self.printNodes(root.right)


if __name__ == '__main__':

    root = TreeNode(50)
    root = PrintAllNodes().insert_node(root, 30)
    root = PrintAllNodes().insert_node(root, 20)
    root = PrintAllNodes().insert_node(root, 40)
    root = PrintAllNodes().insert_node(root, 70)
    root = PrintAllNodes().insert_node(root, 60)
