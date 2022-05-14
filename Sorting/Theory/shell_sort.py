class shell():

    def __init__(self, A):
        self.A = A

    def swap(self, A, x, y):
        temp = A[x]
        A[x] = A[y]
        A[y] = temp

    def ShellSort(self, A, n):
        gap = int(n/2)

        while gap >= 1:
            j = gap
            while j < n:
                i = j-gap
                while i >= 0:
                    if A[i+gap] > A[i]:
                        break

                    else:
                        self.swap(A, i+gap, i)

                    i = i-gap
                j = j + 1
            gap = int(gap/2)

A = []
n = int(input("Enter no of elements in the array \n"))

for i in range(0, n):
    e = int(input("Enter element \n"))
    A.append(e)

sort = shell(A)
sort.ShellSort(A, n)
print(A)

