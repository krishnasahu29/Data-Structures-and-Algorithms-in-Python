# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


head = ListNode(1)
sec = ListNode(1)
th = ListNode(2)

head.next = sec
sec.next = th
th.next = None

print(Solution().deleteDuplicates(head))
