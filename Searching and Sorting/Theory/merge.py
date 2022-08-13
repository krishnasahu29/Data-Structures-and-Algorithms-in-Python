class Merge:

    def __init__(self, arr):
        self.arr = arr

    def MergeSort(self, arr):
        if len(arr) > 1:
            mid = int(len(arr) // 2)
            left_half = arr[:mid]
            right_half = arr[mid:]
            self.MergeSort(left_half)
            self.MergeSort(right_half)

            i = 0
            j = 0
            k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i = i + 1

                else:
                    arr[k] = right_half[j]
                    j = j + 1

                k = k + 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j = j + 1
                k = k + 1

        return arr


if __name__ == '__main__':

    arr = []
    n = int(input("Enter no of elements \n"))

    for i in range(0, n):
        e = int(input("Enter element \n"))
        arr.append(e)
        
    sort = Merge(arr)
    print(sort.MergeSort(arr))

    print(arr)
