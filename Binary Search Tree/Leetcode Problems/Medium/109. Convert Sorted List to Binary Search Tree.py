# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        res = self.traverse_ll(head)
        root = self.sortedArrToBST(res)

        return root

    def traverse_ll(self, head: ListNode):
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res

    def sortedArrToBST(self, arr):
        if not arr:
            return None

        mid = (len(arr)) // 2

        root = TreeNode(arr[mid])

        root.left = self.sortedArrToBST(arr[:mid])

        root.right = self.sortedArrToBST(arr[mid + 1:])
        return root
