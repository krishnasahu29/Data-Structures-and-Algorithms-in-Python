# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# HASH TABLE IMPLEMENTATION
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_table = {}

        temp = head
        while temp:
            if temp in hash_table.keys():
                return temp

            else:
                hash_table[temp] = [temp.next]

            temp = temp.next

        return None

'''

# TWO POINTER IMPLEMENTATION
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                p1 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
