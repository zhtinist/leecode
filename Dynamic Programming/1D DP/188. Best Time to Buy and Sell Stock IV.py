"""
LeetCode #188 - Best Time to Buy and Sell Stock IV
中文题名：买卖股票的最佳时机 IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell
the stock before you buy again).

Example 1:
    Input: prices = [2, 4, 1], k = 2
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
    Input: prices = [3, 2, 6, 5, 0, 3], k = 2
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
    Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

【中文翻译】
给定一个数组，第 i 个元素表示第 i 天的股票价格。设计算法求最大利润，最多可完成 k 笔交易。

注意：同一时刻最多只能持有一股股票，即卖出后才能再次买入。

示例 1：
    输入：prices = [2, 4, 1], k = 2
    输出：2
    解释：第 1 天买入（价格 2），第 2 天卖出（价格 4），利润 4 - 2 = 2。

示例 2：
    输入：prices = [3, 2, 6, 5, 0, 3], k = 2
    输出：7
    解释：第 2 天买入（价格 2），第 3 天卖出（价格 6），利润 4；
          第 5 天买入（价格 0），第 6 天卖出（价格 3），利润 3。
"""

from typing import List, Optional


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # If k >= n/2, it's equivalent to unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # dp[i][j] = max profit on day i with at most j transactions
        # dp_hold[j] = max profit holding a stock with at most j transactions
        dp_hold = [-float("inf")] * (k + 1)
        dp_sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                dp_hold[j] = max(dp_hold[j], dp_sell[j - 1] - price)
                dp_sell[j] = max(dp_sell[j], dp_hold[j] + price)

        return dp_sell[k]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 动态规划。使用两个一维数组滚动更新：
# - dp_hold[j]：进行了 j 次交易后，当前持有股票的最大利润
# - dp_sell[j]：进行了 j 次交易后，当前不持有股票的最大利润
#
# 状态转移：
# - dp_hold[j] = max(保持持有, 买入) = max(dp_hold[j], dp_sell[j-1] - price)
# - dp_sell[j] = max(保持不持有, 卖出) = max(dp_sell[j], dp_hold[j] + price)
#
# 当 k >= n/2 时，等价于可以无限次交易（贪心：收集所有上涨差价）。
#
# 时间复杂度: O(N * K) — 每天每笔交易
# 空间复杂度: O(K) — 两个长度为 K+1 的数组
#
# 关键点:
# - k >= n/2 时退化为贪心（无限交易问题）
# - dp_hold 初始化为负无穷表示不可能的状态
# - 内层循环从 1 到 k，每笔交易依次更新
