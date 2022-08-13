class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Traversal:
    def postorder(self, root: TreeNode):
        if root is None:
            return

        # Create two stacks
        s1 = []
        s2 = []

        # Push root to first stack
        s1.append(root)

        # Run while first stack is not empty
        while s1:

            # Pop an item from s1 and
            # append it to s2
            node = s1.pop()
            s2.append(node)

            # Push left and right children of
            # removed item to s1
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

            # Print all elements of second stack
        while s2:
            node = s2.pop()
            print(node.data, end=" ")


if __name__ == '__main__':

    a: TreeNode = TreeNode('a')
    b: TreeNode = TreeNode('b')
    c: TreeNode = TreeNode('c')
    d: TreeNode = TreeNode('d')
    e: TreeNode = TreeNode('e')
    f: TreeNode = TreeNode('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    Traversal().postorder(a)
