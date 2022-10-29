"""
https://leetcode.com/problems/clone-graph/description/

133. Clone Graph

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

        1 - 2
        |   |
        4 - 3
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_nodes = {}
        new_nodes = {}

        def bfs(start_node) -> None:
            queue = deque([start_node])
            old_nodes[start_node.val] = start_node
            new_nodes[start_node.val] = Node(start_node.val)
            while queue:
                curr_node = queue.popleft()
                for neighbor in curr_node.neighbors:
                    if neighbor.val not in old_nodes:
                        queue.append(neighbor)
                        old_nodes[neighbor.val] = neighbor
                        new_nodes[neighbor.val] = Node(neighbor.val)

        if node:
            bfs(node)

        for old_node in old_nodes.values():
            for neighbor in old_node.neighbors:
                new_neighbor = new_nodes[neighbor.val]
                new_nodes[old_node.val].neighbors.append(new_neighbor)
        
        if node:
            return new_nodes[1]