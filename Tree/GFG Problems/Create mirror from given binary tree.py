# https://www.geeksforgeeks.org/create-a-mirror-tree-from-the-given-binary-tree/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Mirror_Binary_Tree:
    def mirrorify(self, root: Node, mirror) -> Node:
        if not root:
            mirror = None
            return mirror

        mirror = Node(root.val)
        mirror.left = self.mirrorify(root.right, mirror.left)
        mirror.right = self.mirrorify(root.left, mirror.right)

        return mirror


if __name__ == '__main__':
    pass
