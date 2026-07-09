"""
LeetCode #123 - Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

You are given an array prices where prices[i] is the price of a given stock on
the ith day. Find the maximum profit you can achieve with at most two transactions.

Example 1:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6

Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4

Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float("inf")
        profit1 = profit2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)

        return profit2
