"""
46. Permutations
https://leetcode.com/problems/permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
      unused = set(nums)
      result = []
      build = []
      def helper() -> None:
        if not unused:
          result.append(build[:])
          return
        for num in list(unused):
          build.append(num)
          unused.remove(num)
          helper()
          build.pop()
          unused.add(num)
        return

      helper()
      return result
  
solver = Solution()
print(solver.permute([1,2,3]))
print(solver.permute([0,1]))
print(solver.permute([1]))