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
        pass_days = [1, 7, 30]
        table = [0]*(len(days)+1)
        for i, day in enumerate(days):
            candidates = []
            for p, c in zip(pass_days, costs):
                j = bisect.bisect(days, day-p, 0, i)
                candidates.append(table[j]+c)
            table[i+1] = min(candidates)
        return table[-1]
    
if __name__ == "__main__":
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2,7,15]
    solver = Solution()
    print(solver.mincostTickets(days, costs))