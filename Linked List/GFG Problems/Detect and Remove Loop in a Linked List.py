# https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/

class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class DetectandRemove:
    def detectCycle(self, head):
        slow: ListNode = head
        fast: ListNode = head

        while fast or fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow

        return None

    def detectFirstNode(self, head):
        meet: ListNode = self.detectCycle(head)
        start: ListNode = head

        while start != meet:
            start = start.next
            meet = meet.next

        return start
