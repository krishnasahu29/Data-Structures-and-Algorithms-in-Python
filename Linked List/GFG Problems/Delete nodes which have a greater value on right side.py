# https://www.geeksforgeeks.org/delete-nodes-which-have-a-greater-value-on-right-side/

class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None


def reverse(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def delete_lesser_node(head: ListNode) -> ListNode:
    curr = head
    maxNode = head

    while not curr and not curr.next:
        if curr.next.data < maxNode.data:
            temp: ListNode = curr.next
            curr.next = temp.next

        else:
            curr = curr.next
            maxNode = curr

        return head

def delete_right_node(head: ListNode) -> ListNode:
    reverse(head)
    delete_lesser_node(head)
    reverse(head)

    return head

def push(head, new_data):
    new_node = ListNode(new_data)
    new_node.next = head
    head = new_node
    return head

# Utility function to print the linked LinkedList
def display(head):
    curr = head
    while curr is not None:
        print(curr.data, "->", end=" ")
        curr = curr.next

    print("None")


if __name__ == '__main__':
    head: ListNode = None
    head = push(head, 50)
    head = push(head, 40)
    head = push(head, 30)
    head = push(head, 20)
    head = push(head, 10)

    display(head)
    reverse(head)
    display(head)
