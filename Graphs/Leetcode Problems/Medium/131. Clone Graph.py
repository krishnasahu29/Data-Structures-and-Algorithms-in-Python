# https://leetcode.com/problems/clone-graph/

# Definition for a Node.

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        note:
        1. python user-defined classes are hashed
        2. inner function does not re-assign external variable 'cache', but modifies it which is allowed
        :param node:
        :return:
        """

        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None
