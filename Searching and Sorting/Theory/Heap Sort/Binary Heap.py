class BinaryHeap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekofHeap(root: BinaryHeap):
    if not root:
        return

    else:
        return root.customList[1]

def sizeofHeap(root: BinaryHeap):
    if not root:
        return

    else:
        return root.heapSize

def levelOrderTraversal(root: BinaryHeap):
    if not root:
        return

    else:
        for i in range(1, root.heapSize + 1):
            print(root.customList[i])

def insert(root: BinaryHeap, index: int, heapType: str):
    pass


if __name__ == '__main__':
    newBinaryHeap = BinaryHeap(5)
    print(sizeofHeap(newBinaryHeap))
