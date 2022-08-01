# https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/
# https://www.youtube.com/watch?v=kvCYxPKpPGg&ab_channel=AnujBhaiya

"""
1 - 2 - 3 - 4 - 5
|           |
6 - 7 - 8   9   10
    |   |   |
    11  12  13  14
        |   |
        15  16 - 17

Result: 1 to 17
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

class Flatten:
    def queue(self, head: ListNode):

        queue = []
        temp = head

        while temp.next or temp.down:
            if not temp.next:
                print(temp.val)

            if not temp.down:
                queue.append(temp)

            if temp.next:
                temp = queue[0]
                print(queue.remove(queue[0].val))

# TODO: Complete the code
