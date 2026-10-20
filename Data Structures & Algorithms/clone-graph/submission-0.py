"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = dict()
        def cloneNode(node):
            if node and node.val:
                val = node.val
            else:
                return node
            if val in visited:
                return visited[val]
            else:
                newNode = Node(node.val, [])
                visited[val] = newNode
                for neighbor in node.neighbors:
                    newNeighbor = cloneNode(neighbor)
                    newNode.neighbors.append(newNeighbor)
                print(val, newNode.neighbors)
            return newNode
        return cloneNode(node)