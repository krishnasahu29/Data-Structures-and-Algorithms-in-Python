class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def topView(root: Node):
    d = {}
    res = []

    def traverse(root, key, level):
        if root:
            if key not in d:
                d[key] = [root.data, level]

            # key with lesser level
            elif d[key][1] > level:
                d[key] = [root.data, level]

            # traverse to left and right tree
            traverse(root.left, key - 1, level + 1)
            traverse(root.right, key + 1, level + 1)

    traverse(root, 0, 0)
    # print elements in order
    for key in sorted(d):
        res.append(d[key][0])

    return res


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    print(topView(root))
