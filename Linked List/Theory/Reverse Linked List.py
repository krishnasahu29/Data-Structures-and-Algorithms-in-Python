class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReverseLinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):

        prev = None
        curr = self.head
        while curr:
            node = curr.next
            curr.next = prev
            prev = curr
            curr = node

        self.head = prev
