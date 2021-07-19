# # Python program to reverse a linked list
# # Time Complexity : O(n)
# # Space Complexity : O(1)
#
# # Node class
#
#
# class ListNode:
#
#     # Constructor to initialize the node object
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#
#     # Function to reverse the linked list
#     def reverse(self, head) -> ListNode:
#
#         prev = None
#         current = head
#         while current is not None:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         head = prev
#
#     def printList(self):
#         temp = self.head
#         while temp:
#             print(temp.val)
#             temp = temp.next
#
#     def isPalindrome(self, head: ListNode) -> bool:
#         return self.head == self.reverse(head)
#
#
# if __name__ == '__main__':
#
#     head = ListNode(1)
#     sec = ListNode(2)
#     th = ListNode(1)
#
#     head.next = sec
#     sec.next = th
#     th.next = None
#
#     obj = LinkedList()
#     obj.printList()
#     obj.reverse(head)
#     obj.printList()
#     print(obj.isPalindrome(head=head))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverse(self, head) -> ListNode:
        prev = None
        current = head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev

        return head

    def isPalindrome(self, head: ListNode) -> bool:
        return head == self.reverse(head)

    def print(self, head):
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next

if __name__ == '__main__':
    head = ListNode(1)
    sec = ListNode(1)
    th = ListNode(2)

    head.next = sec
    sec.next = th
    th.next = None

    obj = Solution()
    obj.print(head)
    obj.reverse(head)
    obj.print(head)
    print(obj.isPalindrome(head))
