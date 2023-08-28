"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/description/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

        1 - 2
        |   |
        4 - 3
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None # type: ignore
        visited = {}
        queue = deque()
        new_start = Node(node.val)
        visited[node] = new_start
        queue.append(node)
        while queue:
            curr_old = queue.popleft()
            for neighbor in curr_old.neighbors:
                if neighbor not in visited:
                    new_neighbor = Node(neighbor.val)
                    visited[neighbor] = new_neighbor
                    queue.append(neighbor)
                visited[curr_old].neighbors.append(visited[neighbor])

        return new_start