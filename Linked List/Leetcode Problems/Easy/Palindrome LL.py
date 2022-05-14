# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def sum_linkedlist(self, head: ListNode):
        node = head
        n: str = ""
        while node is not None:
            n = n + str(node.val)
            node = node.next

            return n == n[::-1]

    def isPalindrome(self, head: ListNode) -> bool:
        lst: List = []

        node = head
        while node is not None:
            lst.append(node.val)
            node = node.next

        return lst == list(reversed(lst))

if __name__ == '__main__':
    first = ListNode(1)
    sec = ListNode(2)
    th = ListNode(2)
    four = ListNode(1)

    first.next = sec
    sec.next = th
    th.next = four
    four.next = None

    print(Solution().isPalindrome(first))
