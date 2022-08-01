from collections import deque


def queue():
    q = deque()
    q.append(2)
    print(q)
    q.appendleft(1)
    print(q)
    q.append(3)
    print(q)
    q.pop()
    print(q)
    q.popleft()
    print(q)


if __name__ == '__main__':
    queue()
