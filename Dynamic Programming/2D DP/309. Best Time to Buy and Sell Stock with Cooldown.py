"""
LeetCode #309 - Best Time to Buy and Sell Stock with Cooldown
中文题名：最佳买卖股票时机含冷冻期
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Say you have an array for which the ith element is the price of a given
stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you
like (ie, buy one and sell one share of the stock multiple times) with the following
restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the
stock before you buy again).

After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

【中文翻译】
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格。

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）：

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票（即冷冻期为 1 天）。

示例：

输入：[1,2,3,0,2]
输出：3
解释：对应的交易状态为：[买入, 卖出, 冷冻期, 买入, 卖出]
"""

from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        hold = -prices[0]   # 持有股票状态的最大收益
        sold = 0            # 刚卖出（处于冷冻期）状态的最大收益
        rest = 0            # 无股票且不在冷冻期状态的最大收益
        for i in range(1, len(prices)):
            prev_sold = sold
            hold = max(hold, rest - prices[i])
            sold = hold + prices[i]
            rest = max(rest, prev_sold)
        return max(sold, rest)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 状态机动态规划。每天结束时可能处于三种状态之一：
# - hold：持有股票。转移来源：(1) 前一天就持有 hold，(2) 当天买入 rest - price
# - sold：刚卖出股票（处于冷冻期）。只能由前一天持有股票并在当天卖出转移而来：hold + price
# - rest：不持有股票且不在冷冻期。转移来源：(1) 前一天就处于 rest，(2) 前一天刚卖出（冷冻期结束）
#   即 rest = max(rest, prev_sold)，其中 prev_sold 是上一天的 sold 值
# 遍历完成后，最后一天不可能持有股票（卖出才能获得更高利润），答案为 max(sold, rest)
#
# 时间复杂度: O(n) - 一次线性遍历
# 空间复杂度: O(1) - 仅使用常量个变量，优化掉 DP 数组
#
# 关键点:
# - 冷冻期引入第三种状态 sold（刚卖出），与普通无股票状态 rest 区分
# - 状态转移需保存 prev_sold，因为 sold 会在当轮被更新，而 rest 需要的是上一天的 sold
# - 与 #122（无限交易无冷冻期）只多了一个约束，却需要多一个状态
# - 也可用二维 DP dp[i][0/1/2] 实现，但空间可优化为 O(1)
