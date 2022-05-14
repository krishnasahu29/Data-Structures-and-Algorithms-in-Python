class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def length(self):
        c = 0
        node = self.head
        while node is not None:
            node = node.next
            c += 1

        return c

    def insert_beg(self, val):

        node = ListNode(val)
        if self.head is None:
            self.head = node

        else:
            node.next = self.head
            self.head = node

    def insert_end(self, val):
        node = ListNode(val)

        if self.head is None:
            self.head = node

        else:

            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = node

    def delete_beg(self):
        if self.head is None:
            print("Linked List is empty")

        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")

        else:
            temp = self.head

            while temp.next.next is not None:
                temp = temp.next

            temp.next = None

    def delete_pos(self, pos):

        if self.head is None:
            print("Linked List empty")
            return

        if pos == 1:
            self.delete_beg()

        elif pos == self.length():
            self.delete_end()

        else:
            temp = self.head
            for i in range(1, pos - 1):
                temp = temp.next

            next = temp.next.next
            temp.next = None
            temp.next = next

    def print_list(self):

        print("Linked List is: ")
        temp = self.head
        while temp.next is not None:
            print(temp.val, end=" -> ")
            temp = temp.next

        print(temp.val)


if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_beg(1)
    obj.insert_end(2)
    obj.insert_end(3)
    obj.insert_end(4)
    obj.insert_end(5)
    obj.insert_end(6)
    obj.insert_end(7)
    obj.insert_end(8)
    obj.insert_end(9)
    obj.print_list()
    obj.delete_beg()
    obj.print_list()
    obj.delete_pos(7)
    obj.print_list()
    obj.delete_end()
    obj.print_list()
