class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.helper(val, self.root)

    def helper(self, val, curr=TreeNode()):
        if val < curr.val:
            if curr.left is None:
                curr.left = TreeNode(val)
            else:
                self.helper(val, curr.left)

        elif val > curr.val:
            if curr.right is None:
                curr.right = TreeNode(val)
            else:
                self.helper(val, curr.right)

        else:
            print("Value is already present")

    def search(self, val):
        if self.root:
            found = self.search_helper(val, self.root)
            if found:
                return True
            return False
        else:
            return None

    def search_helper(self, val, curr=TreeNode()):
        if val > curr.val and curr.right:
            return self.search_helper(val, curr.right)

        elif val < curr.val and curr.left:
            return self.search_helper(val, curr.left)

        if val == curr.val:
            return True


if __name__ == '__main__':
    BST = BinarySearchTree()
    BST.insert(4)
    BST.insert(2)
    BST.insert(8)
    BST.insert(5)
    BST.insert(10)

    print(BST.search(11))
    print(BST.search(5))
    print(BST.search(7))
