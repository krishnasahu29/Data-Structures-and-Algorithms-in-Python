class quick:

    def __init__(self, A):
        self.A = A

    def Partition(self, A, low, high):
        pivot = A[low]
        start = low
        end = high

        while start < end:
            while A[start] <= pivot:
                start = start + 1

            while A[end] > pivot:
                end = end - 1

            if start < end:
                self.swap(A, start, end)

        self.swap(A, low, end)
        return end

    def swap(self, A, x, y):
        temp = A[x]
        A[x] = A[y]
        A[y] = temp

    def QuickSort(self, A, low, high):
        if low < high:
            loc = self.Partition(A, low, high)
            self.QuickSort(A, low, loc - 1)
            self.QuickSort(A, loc + 1, high)

mylist = []

n = int(input("Enter no of elements \n"))

for i in range(0, n):
    ele = int(input("Enter element \n"))

    mylist.append(ele)
    
sort = quick(mylist)
sort.QuickSort(mylist, 0, len(mylist) - 1)
print(mylist)
