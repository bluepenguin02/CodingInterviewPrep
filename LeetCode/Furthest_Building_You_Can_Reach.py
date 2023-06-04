"""
1642. Furthest Building You Can Reach
https://leetcode.com/problems/furthest-building-you-can-reach/description/

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

* If the current building's height is greater than or equal to the next building's height, you do not need a ladder
or bricks.

* If the current building's height is less than the next building's height, you can either use one ladder or
(h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
"""

import heapq

class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        heap = []
        remain_ladders = ladders
        remain_bricks = bricks
        furthest = -1

        for furthest in range(len(heights)-1):
            diff = heights[furthest+1] - heights[furthest]
            if diff > 0:
                if remain_ladders > 0:
                    remain_ladders -= 1
                    heapq.heappush(heap, diff)
                else:
                    heapq.heappush(heap, diff)
                    if remain_bricks >= heap[0]:
                        remain_bricks -= heapq.heappop(heap)
                    else:
                        return furthest

        return furthest+1
    
solver = Solution()
print(solver.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))