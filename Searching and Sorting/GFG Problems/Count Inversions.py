# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

class Solution:
    # User function Template for python3

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):

        i = 0
        j = len(arr) - 1
        c = 0

        while i < j:
            if arr[i] > arr[j]:
                c += 1

            if j - i == 1:
                i += 1
                j = len(arr) - 1

            else:
                j -= 1

        return c


if __name__ == '__main__':
    arr = [10, 10, 10]
    N = len(arr)
    print(Solution().inversionCount(arr, N))
