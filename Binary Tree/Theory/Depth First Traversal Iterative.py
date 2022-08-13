class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class DepthFirstTraversal:
    def DFS(self, root: TreeNode) -> list:
        result = []
        stack = [root]

        if not root:
            return []

        while len(stack) > 0:
            curr: TreeNode = stack.pop()
            result.append(curr.val)

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        return result


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

    print(DepthFirstTraversal().DFS(a))
