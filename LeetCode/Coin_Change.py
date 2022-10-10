"""
https://leetcode.com/problems/coin-change/description/

322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


class Solution:

    # tabular, slower but more memory efficient
    def coinChange(self, coins: list[int], amount: int) -> int:
        change = [float('inf')] * (amount+1)
        change[0] = 0

        for curr_amount in range(amount):
            for coin in coins:
                new_amount = curr_amount + coin
                if new_amount <= amount:
                    change[new_amount] = min(change[new_amount], change[curr_amount]+1)
        
        return -1 if change[amount] == float('inf') else change[amount]

    # recursive
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}

        def helper(change: int) -> int:
            if change in memo:
                return memo[change]

            if change == 0:
                return 0

            if change < 0:
                return float('inf')

            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1 + helper(change - coin))

            memo[change] = min_coins
            return min_coins

        min_coins = helper(amount)
        return min_coins if min_coins != float('inf') else -1