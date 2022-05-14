# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverse(self, node) -> ListNode:
        prev = None
        current = node
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        node = prev

        return node

    def lst2link(self, lst: List):
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        temp1 = Solution().reverse(l1)
        temp2 = Solution().reverse(l2)

        node = ListNode()

        n1 = 0
        n2 = 0

        while temp1 is not None:
            n1 = n1 * 10 + temp1.val
            temp1 = temp1.next

        while temp2 is not None:
            n2 = n2 * 10 + temp2.val
            temp2 = temp2.next

        s = n1 + n2
        lst = [int(d) for d in str(s)]
        node = Solution().lst2link(lst)
        node = Solution().reverse(node)

        return node
