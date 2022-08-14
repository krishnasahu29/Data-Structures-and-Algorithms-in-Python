class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def mergeArray(a, b):
    ans = []
    i, j = 0, 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1

        else:
            ans.append(b[j])
            j += 1

    while i < len(a):
        ans.append(a[i])
        i += 1

    while j < len(b):
        ans.append(b[j])
        j += 1

    return ans

def inordertoBST(s, e, res) -> TreeNode:
    if s > e:
        return None
    mid = (s + e) // 2
    root = TreeNode(res[mid])
    root.left = inordertoBST(s, mid - 1, res)
    root.right = inordertoBST(mid + 1, e, res)
    return root

def inorder(root, res):
    if not root:
        return

    else:
        inorder(root.left, res)
        res.append(root.data)
        inorder(root.right, res)

def mergeBST(root1: TreeNode, root2: TreeNode) -> TreeNode:
    bst1, bst2 = [], []
    inorder(root1, bst1)
    inorder(root2, bst2)

    mergeArr = mergeArray(bst1, bst2)
    return inordertoBST(0, len(mergeArr) - 1, mergeArr)
