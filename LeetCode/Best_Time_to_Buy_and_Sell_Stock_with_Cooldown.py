"""
309. Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock
before you buy again).
"""

from functools import cache

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
      @cache
      def helper(index: int, owned: bool) -> int:
        if index >= len(prices):
          return 0
        if owned:
          a = helper(index+2, False) + prices[index]
          b = helper(index+1, True)
          return max(a,b)
        else:
          a = helper(index+1, True) - prices[index]
          b = helper(index+1, False)
          return max(a,b)

      return helper(0, False)
  

solver = Solution()
print(solver.maxProfit([1,2,3,0,2]))
print(solver.maxProfit([1,2,3,0,2,1,3]))