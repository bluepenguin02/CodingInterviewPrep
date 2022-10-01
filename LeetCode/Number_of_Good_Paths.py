"""
https://leetcode.com/problems/number-of-good-paths/

2421. Number of Good Paths

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer
array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's
value should be the maximum value along the path).

Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node
is also considered as a valid path.


Note:
This can be done via depth-first-search, but I get time limit exceeded with that method, even if others don't.
"""

from collections import Counter

class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        num_paths = len(vals)
        valued_edges = [(max(vals[u], vals[v]), u, v) for u, v in edges]
        valued_edges.sort()
        unions = UnionFind(len(vals))
        count = [Counter({vals[i]: 1}) for i in range(len(vals))]
        
        for val, u, v in valued_edges:
            leader_u = unions.find(u)
            leader_v = unions.find(v)
            count_l_u = count[leader_u][val]
            count_l_v = count[leader_v][val]
            num_paths += count_l_u * count_l_v
            new_leader = unions.union(leader_u, leader_v)
            count[new_leader] = Counter({val: count_l_u + count_l_v})
            
        return num_paths
    
    
class UnionFind:
    def __init__(self, size: int):
        self.parents = list(range(size))
        self.rank = [0] * size
        
    def union(self, elem1: int, elem2: int) -> int:
        leader1 = self.find(elem1)
        leader2 = self.find(elem2)
        if self.rank[leader1] > self.rank[leader2]:
            self.parents[leader2] = leader1
            new_leader = leader1
        else: 
            self.parents[leader1] = leader2
            new_leader = leader2
            if self.rank[leader1] == self.rank[leader2]:
                self.rank[leader2] += 1
        return new_leader
        
    def find(self, elem) -> int:
        leader = elem
        while leader != self.parents[leader]:
            leader = self.parents[leader]
        return leader