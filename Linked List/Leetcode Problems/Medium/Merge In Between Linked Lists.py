# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def traverse(self, node: ListNode):
        while node.next is not None:
            node = node.next

        return node.next

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1
        k = 0
        while start is not None:
            if k == a - 1:
                fur = start.next
                start.next = list2
                start2 = list2
                while start2.next is not None:
                    start2 = start2.next
                k2 = a
                while fur is not None:
                    if k2 == b:
                        if fur.next is not None:
                            start2.next = fur.next
                        else:
                            start2.next = None
                    k2 += 1
                    fur = fur.next
                return list1
            k += 1
            start = start.next
