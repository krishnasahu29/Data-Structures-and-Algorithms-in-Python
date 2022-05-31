class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeTwoLinkedList:

    # @staticmethod
    def mergeSorted(self, l1: ListNode, l2: ListNode):
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeSorted(l1.next, l2)
            return l1

        else:
            l2.next = self.mergeSorted(l1, l2.next)
            return l2

    # @staticmethod
    def printLinkedList(self, node: ListNode):
        temp = node
        while temp is not None:
            print(temp.val, end=" ")


if __name__ == '__main__':
    n1: ListNode = ListNode(1)
    n2: ListNode = ListNode(5)
    n3: ListNode = ListNode(13)
    n4: ListNode = ListNode(14)
    n5: ListNode = ListNode(550)

    n1_1: ListNode = ListNode(2)
    n2_1: ListNode = ListNode(15)
    n3_1: ListNode = ListNode(130)
    n4_1: ListNode = ListNode(200)
    n5_1: ListNode = ListNode(350)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    n1_1.next = n2_1
    n2_1.next = n3_1
    n3_1.next = n4_1
    n4_1.next = n5_1
    n5_1.next = None

    obj = MergeTwoLinkedList()
    Sorted = obj.mergeSorted(n1, n1_1)
    obj.printLinkedList(Sorted)
