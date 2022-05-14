# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> object:
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == '__main__':

    head = ListNode(1)
    sec = ListNode(2)
    th = ListNode(2)
    four = ListNode(3)
    fifth = ListNode(5)

    head.next = sec
    sec.next = th
    th.next = four
    four.next = fifth
    fifth.next = None

    s = Solution()
    s.deleteDuplicates(head)
