# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        a_pt: ListNode = headA
        b_pt: ListNode = headB
        while a_pt != b_pt:
            if a_pt is None:
                a_pt = headB

            else:
                a_pt = a_pt.next

            if b_pt is None:
                b_pt = headA

            else:
                b_pt = b_pt.next

        return a_pt


if __name__ == '__main__':
    head1 = ListNode(4)
    b1 = ListNode(1)
    head2 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(1)
    c1 = ListNode(8)
    c2 = ListNode(4)

    head1.next = b1
    b1.next = c1
    head2.next = b2
    b2.next = b3
    b3.next = c1
    c1.next = c2
    c2.next = None

    print(Solution().getIntersectionNode(head1, head2))
