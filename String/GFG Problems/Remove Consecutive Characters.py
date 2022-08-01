# https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1

class Solution:
    def removeConsecutiveCharacter(self, S):
        stack = []
        p = None
        for i in S:
            if i != p:
                stack.append(i)
                p = i

        return "".join(stack)


if __name__ == '__main__':
    print(Solution().removeConsecutiveCharacter('aabbaaccc'))
