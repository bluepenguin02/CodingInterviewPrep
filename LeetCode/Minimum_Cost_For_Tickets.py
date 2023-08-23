"""
983. Minimum Cost For Tickets

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.
"""

import bisect

class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
      price = [0] * days[-1]
      days_set = set(days)
      
      for day in range(days[-1]):
        if day+1 in days_set:
          d1 = price[day - 1] + costs[0] if day - 1 >= 0 else costs[0]
          d7 = price[day - 7] + costs[1] if day - 7 >= 0 else costs[1]
          d30 = price[day - 30] + costs[2] if day - 30 >= 0 else costs[2]
          price[day] = min(d1, d7, d30)
        else:
          price[day] = price[day-1]

      return price[-1]
    

solver = Solution()
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(solver.mincostTickets(days, costs))
days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(solver.mincostTickets(days, costs))