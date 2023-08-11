"""
1631. Path With Minimum Effort
https://leetcode.com/problems/path-with-minimum-effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell,
(0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can
move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.


Methodology: Use a variation of Dijkstra's algorithm
"""

import heapq

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        valid_moves = [(-1,0), (1, 0), (0, 1), (0, -1)]
        n_rows = len(heights)
        n_cols = len(heights[0])
        start = (0,0)
        end = (n_rows-1, n_cols-1)

        if start == end:
            return 0

        heap = []
        heapq.heappush(heap, (0, 0, 0))
        seen = [[False]*n_cols for _ in range(n_rows)]

        path_abs_diff = 0
        while heap:
            path_abs_diff, curr_r, curr_c = heapq.heappop(heap)

            if (curr_r, curr_c) == end:
                return path_abs_diff

            if seen[curr_r][curr_c]:
                continue
            seen[curr_r][curr_c] = True
            curr_height = heights[curr_r][curr_c]

            for dr, dc in valid_moves:
                new_r = curr_r+dr
                new_c = curr_c+dc
                if start[0] <= new_r <= end[0] and start[1] <= new_c <= end[1] and \
                    not seen[new_r][new_c]:
                    new_height = heights[new_r][new_c]
                    abs_diff = abs(curr_height - new_height)
                    new_path_abs_diff = max(abs_diff, path_abs_diff)
                    heapq.heappush(heap, (new_path_abs_diff, new_r, new_c))

        return path_abs_diff
  
solver = Solution()
print(solver.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(solver.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
print(solver.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))