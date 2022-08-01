# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

class Solution:
    # User function Template for python3

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        count = 1
        hash_table = {}
        for idx, item in enumerate(arr):
            hash_table[idx] = item

        
