# https://practice.geeksforgeeks.org/problems/8a644e94faaa94968d8665ba9e0a80d1ae3e0a2d/1

class Solution:
    def overlappedInterval(self, intervals):

        intervals.sort()
        stack = [intervals[0]]

        # insert first interval into stack
        for i in intervals[1:]:
            # Check for overlapping interval,
            # if interval overlap
            if stack[-1][0] <= i[0] <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], i[1])

            else:
                stack.append(i)

        return stack


if __name__ == '__main__':
    print(Solution().overlappedInterval([[6, 8], [1, 9], [2, 4], [4, 7]]))
