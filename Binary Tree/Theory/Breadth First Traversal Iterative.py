class TreeNode:
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right


class BreadthFirstTraversal:
    def traversal_iterative(self, root: TreeNode):

        if not root:
            return []

        res = []
        state = [root]

        while len(state) > 0:
            curr: TreeNode = state.pop()
            res.append(curr.val)
            if curr.left:
                state.insert(0, curr.left)

            if curr.right:
                state.insert(0, curr.right)

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
    print(BreadthFirstTraversal().traversal_iterative(a))
