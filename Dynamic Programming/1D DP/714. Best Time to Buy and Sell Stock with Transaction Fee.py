"""
LeetCode #714 - Best Time to Buy and Sell Stock with Transaction Fee
中文题名：买卖股票的最佳时机含手续费
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Your are given an array of integers `prices`, for which the `i`-th
element is the price of a given stock on day `i`; and a non-negative integer
`fee` representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee
for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must
sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:

Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:

Buying at prices[0] = 1

Selling at prices[3] = 8

Buying at prices[4] = 4

Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Note:

`0 < prices.length <= 50000`.

`0 < prices[i] < 50000`.

`0 <= fee < 50000`.

【中文翻译】
给定一个整数数组 `prices`，其中第 `i` 个元素是给定股票在第 `i` 天的价格；以及一个非负整数 `fee` 表示交易手续费。

你可以完成任意多次交易，但每次交易都需要支付交易手续费。你不能同时持有超过一股股票（即必须在再次购买之前卖出股票）。

返回你可以获得的最大利润。

示例 1：

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 最大利润可以通过以下操作实现：

在 prices[0] = 1 时买入

在 prices[3] = 8 时卖出

在 prices[4] = 4 时买入

在 prices[5] = 9 时卖出

总利润为 ((8 - 1) - 2) + ((9 - 4) - 2) = 8。

注意：

`0 < prices.length <= 50000`。

`0 < prices[i] < 50000`。

`0 <= fee < 50000`。
"""

from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -float('inf')
        for price in prices:
            cash = max(cash, hold + price - fee)
            hold = max(hold, cash - price)
        return cash









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划，每天维护两个状态：
# - cash: 当前不持有股票时的最大利润
# - hold: 当前持有一股股票时的最大利润
# 状态转移：
# - cash = max(cash, hold + price - fee)  # 什么都不做 或 卖出（获得 price，支付 fee）
# - hold = max(hold, cash - price)         # 什么都不做 或 买入（花费 price）
# 初始状态：cash = 0（第 0 天不持有），hold = -inf（第 0 天不可能持有）。
# 最终 cash 即为最大利润。
#
# 时间复杂度: O(n) - 一次遍历
# 空间复杂度: O(1) - 仅使用两个变量
#
# 关键点:
# - 与 #122 的区别：卖出时需减去手续费
# - 两个状态（持有/不持有）的 DP
# - 手续费可以加在卖出时，也可以加在买入时，效果等价
# - 无限交易次数，但每次卖出需支付 fee
