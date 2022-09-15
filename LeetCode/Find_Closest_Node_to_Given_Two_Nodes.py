"""
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.
"""


MAX_DIST = 10**6

class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        dists_from_1 = self.find_dists(edges, node1)
        dists_from_2 = self.find_dists(edges, node2)
        common_nodes = list(set(dists_from_1).intersection(set(dists_from_2)))
        common_nodes.sort()
        
        middle_node = -1
        least_max_dist = MAX_DIST
        for node in common_nodes:
            if max(dists_from_1[node], dists_from_2[node]) < least_max_dist:
                middle_node = node
                least_max_dist = max(dists_from_1[node], dists_from_2[node])
        
        return middle_node
                
        
    def find_dists(self, edges: list[int], start: int) -> dict:
        dists = {start: 0}
        node = start
        dist = 0
        while edges[node] != -1 and edges[node] not in dists:
            node = edges[node]
            dist += 1
            dists[node] = dist
        return dists
    
if __name__ == '__main__':
    test = [1,2,-1]
    solu = Solution()
    print(solu.closestMeetingNode(test, 0, 2))