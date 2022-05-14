# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head or not head.next:
            return False

        p1 = head
        p2 = head.next

        while p2:
            p2 = p2.next
            if p2:
                p2 = p2.next
            if not p2:
                return False

            p1 = p1.next

            if p1 == p2:
                return True


if __name__ == '__main__':
    head = ListNode(1)

    head.next = None

    print(Solution().hasCycle(head))
