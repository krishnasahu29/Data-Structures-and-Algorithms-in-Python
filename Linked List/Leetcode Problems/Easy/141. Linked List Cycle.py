# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        cycle_set = set()

        p1 = head
        # p2 = head.next

        while p1.next:
            if p1.next in cycle_set:
                return True

            cycle_set.add(p1.next)

        return False
