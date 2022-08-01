class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class DepthFirstTraversal:
    def DFS_recursive(self, head: TreeNode):

        if not head:
            return []

        leftVals = self.DFS_recursive(head.left)
        rightVals = self.DFS_recursive(head.right)

        res = [head.val]

        res.extend(leftVals)
        res.extend(rightVals)

        return res


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

    print(DepthFirstTraversal().DFS_recursive(a))
