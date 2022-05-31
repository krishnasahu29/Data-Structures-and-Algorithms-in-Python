class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Recursion:

    def reverse(self, head: ListNode):
        if head is None or head.next is None:
            return head

        p: ListNode = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return p


if __name__ == '__main__':
    head = ListNode(1)
    sec = ListNode(1)
    th = ListNode(2)

    head.next = sec
    sec.next = th
    th.next = None

    print(Recursion().reverse(head))
