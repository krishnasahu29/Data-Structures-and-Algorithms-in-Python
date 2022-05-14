# from queue import Empty


class Stack:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        """
        Raise Empty exception if the stack is empty.
        :return: the element at the top of the stack
        """

        if self.is_empty():
            raise 'Stack is empty'

        return self.data[-1]

    def pop(self):
        """
        Raise Empty exception if the stack is empty.
        :return: remove and return from the top of the stack
        """

        if self.is_empty():
            raise "Stack is empty"

        return self.data.pop()
