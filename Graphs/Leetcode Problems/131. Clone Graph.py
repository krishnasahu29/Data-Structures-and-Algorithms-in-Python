# https://leetcode.com/problems/clone-graph/

# Definition for a Node.

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        note:
        1. python user-defined classes are hashed
        2. inner function does not re-assign external variable 'cache', but modifies it which is allowed
        :param node:
        :return:
        """

        if not node:
            return None

        cache = {node: Node(node.val, [])}

        def search(org):
            for suc in org.neighbors:
                if suc not in cache:
                    cache[suc] = Node(suc.val, [])
                    search(suc)
                cache[org].neighbors += cache[suc],

        search(node)
        return cache[node]
