# https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1

class Solution:

    # Function to find the smallest window in the string s consisting of all the characters of string p.
    def smallestWindow(self, s, p):
        # code here
        for i in range(len(s)):
            pass


if __name__ == '__main__':
    print(Solution().smallestWindow('timetopractice', 'toc'))
    d1 = {1: 'a', 2: 'b'}
    d2 = {1: 'a', 2: 'b'}
    d3 = {1: 'a', 3: 'b'}
    print(d1 == d2)
    print(d1 == d3)
