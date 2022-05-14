# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # SOLUTION USING CIRCULAR LL

        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next

        if k > length:
            return head

        for i in range(length - k):
            temp = head
            for j in range(1, length):
                temp = temp.next

            temp.next.next = head.next
            head = temp.next.next
            temp.next = None

        return head



if __name__ == '__main__':
    head = ListNode(1)
    sec = ListNode(2)
    th = ListNode(3)
    four = ListNode(4)
    fifth = ListNode(5)

    head.next = sec
    sec.next = th
    th.next = four
    four.next = fifth
    fifth.next = None

    print(Solution().rotateRight(head, 2))
