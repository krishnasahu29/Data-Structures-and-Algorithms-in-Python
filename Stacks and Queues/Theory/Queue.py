class Queue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * Queue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        """
        Raise Empty exception if the queue is empty.
        :return: element at the front of the queue
        """

        if self.is_empty():
            raise 'Queue is empty'

        return self.data[self.front]

    def dequeue(self):
        """
        Raise Empty exception if the queue is empty.
        :return: remove and return first element in the queue
        """

        if self.is_empty():
            raise 'Queue is empty'

        answer = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return answer

    def resize(self, cap):
        """
        Resize to a new list of capacity >= len(self).
        :param cap: new capacity
        :return: None
        """

        old = self.data
        self.data = [None] * cap
        walk = self.front

        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)

        self.front = 0

    def enqueue(self, e):
        """
        Add element at the back of the queue
        :param e: element to be inserted
        :return: None
        """

        if self.size == len(self.data):
            self.resize(2 * len(self.data))

        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e

        self.size += 1

