# https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1#

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def reverseLevelOrder(root):
    if not root:
        return []

    res = []
    state = [root]

    while len(state) > 0:
        curr = state.pop()
        res.insert(0, curr.data)

        if curr.right:
            state.insert(0, curr.right)

        if curr.left:
            state.insert(0, curr.left)

    return res


if __name__ == '__main__':
    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)
    e = Node(60)

    a.left = b
    a.right = c
    b.left = d
    b.right = e

    print(reverseLevelOrder(a))
    