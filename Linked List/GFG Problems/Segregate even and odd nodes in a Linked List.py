# https://www.geeksforgeeks.org/segregate-even-and-odd-elements-in-a-linked-list/

class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None


def segregate_even_odd(head: ListNode) -> ListNode:
    even: ListNode = None
    odd: ListNode = None

    while not head:
        new_node = ListNode(head.data)
        if head.data % 2 == 0:
            even.next = new_node

        else:
            odd.next = new_node

    added_list: ListNode = ListNode(0)
    while not even:
        node = ListNode(even.data)
        added_list = node
        # if added_list:
        #     added_list = node
        #
        # else:
        #     added_list.next = even
        #     added_list.data = even.data
        #     even = even.next

    while not odd:

        node = ListNode(odd.data)
        added_list = node

        # node = ListNode(odd.data)
        # added_list.next = odd
        # added_list.data = odd.data
        # odd = odd.next

    return added_list


def push(head: ListNode, new_data) -> ListNode:
    tem = ListNode(0)
    tem.data = new_data
    tem.next = head
    head = tem
    return head


def display(head: ListNode) -> None:
    while head.next:
        print(head.data, end='->')
        head = head.next

    print(head.data)


if __name__ == '__main__':
    head: ListNode = None
    head = push(head, 17)
    head = push(head, 15)
    head = push(head, 12)
    head = push(head, 18)

    display(head)
    segregate_even_odd(head)
    display(head)
