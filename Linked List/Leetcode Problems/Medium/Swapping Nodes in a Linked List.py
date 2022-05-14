# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def count_nodes(self, node: ListNode) -> int:

        c = 0
        while node is not None:
            c += 1
            node = node.next

        return c

    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        node = head
        n = self.count_nodes(node) - k

        if n == k:
            return head


if __name__ == '__main__':
    on = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)

    on.next = two
    two.next = three
    three.next = four
    four.next = five
    five = None

    print(Solution().swapNodes(on, 2))
