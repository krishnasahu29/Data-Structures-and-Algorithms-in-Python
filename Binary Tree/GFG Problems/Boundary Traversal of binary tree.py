# https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:

    def traverseLeft(self, root, ans):
        if root is None or (root.left is None and root.right is None):
            return

        ans.append(root.data)
        if root.left:
            self.traverseLeft(root.left, ans)
        else:
            self.traverseLeft(root.right, ans)

    def traverseLeaf(self, root, ans):
        if not root:
            return

        if root.left is None and root.right is None:
            ans.append(root.data)
            return

        self.traverseLeaf(root.left, ans)
        self.traverseLeaf(root.right, ans)

    def traverseRight(self, root, ans):
        if root is None or (root.left is None and root.right is None):
            return

        if root.right:
            self.traverseRight(root.right, ans)
        else:
            self.traverseRight(root.left, ans)

        ans.append(root.data)

    def printBoundaryView(self, root):
        ans = []
        if not root:
            return ans

        ans.append(root.data)

        self.traverseLeft(root.left, ans)

        self.traverseLeaf(root.left, ans)
        self.traverseLeaf(root.right, ans)

        self.traverseRight(root.right, ans)

        return ans


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    print(Solution().printBoundaryView(root))
