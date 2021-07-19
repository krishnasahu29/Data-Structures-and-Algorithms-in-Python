# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(val=None)
        current = head

        # O(n + m)
        while l1 and l2:
            if l1.val <= l2.val:
                next_node = ListNode(l1.val)
                l1 = l1.next
            else:
                next_node = ListNode(l2.val)
                l2 = l2.next
            current.next = next_node
            current = next_node

        # O(n)
        while l1:
            next_node = ListNode(l1.val)
            l1 = l1.next
            current.next = next_node
            current = next_node

        # O(m)
        while l2:
            next_node = ListNode(l2.val)
            l2 = l2.next
            current.next = next_node
            current = next_node

        return head.next


if __name__ == '__main__':
    l1_1 = ListNode(4)
    l1_2 = ListNode(7)
    l1_3 = ListNode(9)

    l1_1.next = l1_2
    l1_2.next = l1_3
    l1_3.next = None

    l2_1 = ListNode(3)
    l2_2 = ListNode(5)
    l2_3 = ListNode(6)

    l2_1.next = l2_2
    l2_2.next = l2_3
    l2_3.next = None

    obj = Solution()
    print(obj.mergeTwoLists(l1_1, l2_1))
