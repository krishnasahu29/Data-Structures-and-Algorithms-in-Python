# https://practice.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def isdeadEnd(root):
    res = []
    res_leaf = []

    def dfs(root):
        stack = [root]

        if not root:
            return []

        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.data)
            if not curr.left and not curr.right:
                res_leaf.append(curr.data)

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        return res

    dfs(root)
    for i in res_leaf:
        if i + 1 in res and i - 1 in res:
            return True

    return False


if __name__ == '__main__':
    root = Node(8)
    root.left = Node(7)
    root.right = Node(10)
    root.left.left = Node(2)
    root.right.left = Node(9)
    root.right.right = Node(13)
    print(isdeadEnd(root))
