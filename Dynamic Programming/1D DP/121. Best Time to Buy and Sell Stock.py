"""
LeetCode #121 - Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on
the ith day. You want to maximize your profit by choosing a single day to buy
and a different day in the future to sell. Return the maximum profit.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
