# https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def reverseDLL(head: Node):

    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        curr.prev = curr.next
        prev = curr
        curr = next

    head = prev
    return head
