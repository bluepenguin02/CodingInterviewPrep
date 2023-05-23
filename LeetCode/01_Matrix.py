"""
542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

"""

from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
      q = deque()
      visited = set()
      dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
      m = len(mat)
      n = len(mat[0])

      for r in range(m):
        for c in range(n):
          if mat[r][c] == 0:
            q.append((r,c))
            visited.add((r,c))

      while q:
        r, c = q.popleft()
        for dr, dc in dirs:
          if 0 <= r+dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in visited:
            mat[r+dr][c+dc] = mat[r][c] + 1
            q.append((r+dr, c+dc))
            visited.add((r+dr, c+dc))

      return mat


solver = Solution()
print(solver.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))