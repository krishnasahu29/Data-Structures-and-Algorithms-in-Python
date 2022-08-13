# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
# Python program to print left view of Binary Tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LeftView(root):
    if not root:
        return []

    D = {}
    queue = [[0, root]]

    while queue:
        cur = queue.pop()
        D[cur[0]] = cur[1].data

        if cur[1].left:
            queue.append([cur[0] + 1, cur[1].left])

        if cur[1].right:
            queue.append([cur[0] + 1, cur[1].right])

    for v in D.values():
        queue.append(v)

    return queue


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)

    print(LeftView(root))
