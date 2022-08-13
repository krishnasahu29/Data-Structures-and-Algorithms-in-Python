# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

class ListNode:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# Driver code
ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(85)

print("Given Linked List")
ll.printList()
ll.reverse()
print("\nReversed Linked List")
ll.printList()

if __name__ == '__main__':
    head = ListNode(1)
    sec = ListNode(1)
    th = ListNode(2)

    head.next = sec
    sec.next = th
    th.next = None
