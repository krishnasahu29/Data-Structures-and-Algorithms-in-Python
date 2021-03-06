class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:

    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begin(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def print(self):
        if self.head is None:
            print("Linked List is Empty")

        else:
            itr = self.head
            llist = ''

            while itr:
                llist += str(itr.data) + '-->' if itr.next else str(itr.data)
                itr = itr.next

            print(llist)


if __name__ == '__main__':
    ll = Linked_list()
    ll.insert_list(['Java', 'C++', 'C', 'Python'])
    ll.print()
    ll.insert_at(1, "Julia")
    ll.print()
    ll.remove(2)
    ll.print()
