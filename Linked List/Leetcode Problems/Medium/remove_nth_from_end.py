# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        c = self.count_nodes(head)
        end = c - n + 1

        if head is None:
            return None

        elif c == n:
            head = head.next
            return head

        elif c == 0:
            temp = head
            while temp.next is not None:
                temp = temp.next

            temp.next = None

        else:
            temp = head

            for i in range(1, end - 1):
                temp = temp.next

            temp.next = temp.next.next

            return head

    def count_nodes(self, node: ListNode):
        c = 0
        while node is not None:
            c += 1
            node = node.next

        return c

if __name__ == '__main__':

    first = ListNode(1)
    sec = ListNode(2)
    th = ListNode(3)
    four = ListNode(4)
    fifth = ListNode(5)

    first.next = sec
    sec.next = th
    th.next = four
    four.next = fifth
    fifth.next = None

    s = Solution()
    s.removeNthFromEnd(first, 2)
