"""
LeetCode #122 - Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

You are given an integer array prices where prices[i] is the price of a given
stock on the ith day. On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share at a time. Return the maximum profit.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7

Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4

Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0

Constraints:
    1 <= prices.length <= 3 * 10^4
    0 <= prices[i] <= 10^4
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
