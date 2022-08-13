# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1

class Solution:
    def kthLargest(self, root, k):
        # your code here
        res = []

        def dfs(root):

            if not root:
                return

            stack = [root]
            while len(stack) > 0:
                curr = stack.pop()
                res.append(curr.data)
                if curr.left:
                    stack.append(curr.left)

                if curr.right:
                    stack.append(curr.right)

            return res

        dfs(root)
        return sorted(res)[-k]


if __name__ == '__main__':
    pass
