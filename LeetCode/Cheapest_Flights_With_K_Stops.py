"""
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops

There are n cities connected by some number of flights. You are given an array flights where
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with
at most k stops. If there is no such route, return -1.

"""

import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, K: int) -> int:
        graph = [[] for _ in range(n)]
        stops = [float('inf') for _ in range(n)]
        for city1, city2, cost in flights:
            graph[city1].append((city2, cost))

        heap = []
        for city2, cost in graph[src]:
            heapq.heappush(heap, (cost, city2, 0))

        while heap:
            cost, city1, layovers = heapq.heappop(heap)
            if city1 == dst:
                return cost
            if layovers < K and stops[city1] >= layovers:
                stops[city1] = layovers
                for city2, leg_cost in graph[city1]:
                    heapq.heappush(heap, (cost+leg_cost, city2, layovers+1))

        return -1
    
solver = Solution()
print(solver.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, K = 1))
print(solver.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1))
print(solver.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0))    