from collections import deque


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Search_Tree:

    def insert_node(self, head: BSTNode, data):

        if head.data is None:
            head.data = data

        elif data <= head.data:
            if head.left:
                self.insert_node(head.left, data)
            else:
                head.left = BSTNode(data)

        else:
            if head.right:
                self.insert_node(head.right, data)
            else:
                head.right = BSTNode(data)
        return head

    def preOrderTraversal(self, head: BSTNode):
        if not head:
            return

        print(head.data, end=' ')
        self.preOrderTraversal(head.left)
        self.preOrderTraversal(head.right)

    def postOrderTraversal(self, head: BSTNode):

        if not head:
            return

        self.postOrderTraversal(head.left)
        self.postOrderTraversal(head.right)
        print(head.data, end=' ')

    def inOrderTraversal(self, head: BSTNode):

        if not head:
            return

        self.inOrderTraversal(head.left)
        print(head.data, end=' ')
        self.inOrderTraversal(head.right)

    def levelOrderTraversal(self, head):

        q = deque([head])
        if not head:
            return 0

        while q:

            for i in range(len(q)):
                node = q.popleft()
                print(node.data, end=' ')

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

    def search(self, head: BSTNode, val):

        if head.data == val or head is None:
            return True

        if head.data < val:
            return self.search(head.right, val)

        return self.search(head.left, val)

    def getMinimumKey(self, curr: BSTNode):
        while curr.left:
            curr = curr.left
        return curr

    def deletion(self, root: BSTNode, val):
        parent = None
        curr = root

        while curr and curr.data != val:
            parent = curr

            if val < curr.data:
                curr = curr.left

            else:
                curr = curr.right

        if curr is None:
            return root

        # Case 1: node to be deleted is a leaf node
        if not curr.left and not curr.right:
            if curr != root:
                if parent.left == curr:
                    parent.left = None

                else:
                    parent.right = None

            else:
                root = None

        # Case 2: Node to be deleted has 2 children
        elif curr.left and curr.right:

            # find its inorder successor node
            successor = self.getMinimumKey(curr.right)

            # store successor node
            val = successor.data

            # recursively delete the successor. Note that the successor
            # will have at most one child (right child)
            self.deletion(root, successor.data)

            # copy value of the successor to the current node
            curr.data = val

        # Case 3: node to be deleted has only one child
        else:

            # choose a child node
            if curr.left:
                child = curr.left
            else:
                child = curr.right

            # if the node to be deleted is not a root node, set its parent to its child
            if curr != root:
                if curr == parent.left:
                    parent.left = child
                else:
                    parent.right = child

            # if the node to be deleted is a root node, then set the root to the child
            else:
                root = child

        return root


if __name__ == '__main__':
    head = BSTNode(None)
    print(Binary_Search_Tree().insert_node(head, 10))
    print(Binary_Search_Tree().insert_node(head, 4))
    print(Binary_Search_Tree().insert_node(head, 6))
    print(Binary_Search_Tree().insert_node(head, 15))
    Binary_Search_Tree().inOrderTraversal(head)
    Binary_Search_Tree().deletion(head, 4)
    Binary_Search_Tree().inOrderTraversal(head)
