"""
957. Prison Cells After N Days
https://leetcode.com/problems/prison-cells-after-n-days

There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:
* If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
* Otherwise, it becomes vacant.

Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the
ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).

"""


class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:

      def next_day(cellsA: list, cellsB: list) -> list:
        for i in range(1, len(cellsA)-1):
          cellsB[i] = 1 ^ cellsA[i-1] ^ cellsA[i+1]
        return cellsB

      cells1 = cells
      cells2 = [0]*len(cells)
      day1 = tuple(next_day(cells1, cells2))
      cells1 = cells2

      if n == 1:
        return list(day1)
      
      day = (0, 0)
      counter = 0
      cells2 = [0]*len(cells)
      while day != day1 and counter < n-1:
        day = tuple(next_day(cells1, cells2))
        cells1, cells2 = cells2, cells1
        counter += 1

      limit = (n-1) % counter
      for _ in range(limit):
        day = tuple(next_day(cells1, cells2))
        cells1, cells2 = cells2, cells1

      return list(day)
  
solver = Solution()
print(solver.prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], n = 7))
print(solver.prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], n = 1000000000))