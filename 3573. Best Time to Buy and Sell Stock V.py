"""
LeetCode #3573 - Best Time to Buy and Sell Stock V
买卖股票的最佳时机 V
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-v/

给你一个整数数组 `prices`，其中 `prices[i]` 是第 `i` 天股票的价格（美元），以及一个整数 `k`。
你最多可以进行 `k` 笔交易，每笔交易可以是以下任一类型：

普通交易：在第 `i` 天买入，然后在之后的第 `j` 天卖出，其中 `i < j`。你的利润是 `prices[j] - prices[i]`。

做空交易：在第 `i` 天卖出，然后在之后的第 `j` 天买回，其中 `i < j`。你的利润是 `prices[i] - prices[j]`。
注意：你必须在开始下一笔交易之前完成当前交易。此外，你不能在已经进行买入或卖出操作的同一天再次进行买入或卖出操作。
通过进行 最多 `k` 笔交易，返回你可以获得的最大总利润。

示例 1:

输入: prices = [1,7,9,8,2], k = 2
输出: 14
解释: 我们可以通过 2 笔交易获得 14 美元的利润：
一笔普通交易：第 0 天以 1 美元买入，第 2 天以 9 美元卖出。
一笔做空交易：第 3 天以 8 美元卖出，第 4 天以 2 美元买回。
示例 2:

输入: prices = [12,16,19,19,8,1,19,13,9], k = 3
输出: 36
解释: 我们可以通过 3 笔交易获得 36 美元的利润：
一笔普通交易：第 0 天以 12 美元买入，第 2 天以 19 美元卖出。
一笔做空交易：第 3 天以 19 美元卖出，第 4 天以 8 美元买回。
一笔普通交易：第 5 天以 1 美元买入，第 6 天以 19 美元卖出。

提示:
`2 <= prices.length <= 10^3`
`1 <= prices[i] <= 10^9`
`1 <= k <= prices.length / 2`
"""

from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        INF = float('-inf')

        # dp[t][state]:
        # state 0: 空仓（手中无股票，无做空）
        # state 1: 持有股票（做多中）
        # state 2: 做空持仓（借股卖出后，待买回）
        # t 表示已完成 t 笔交易（0 <= t <= k）
        dp_empty = [INF] * (k + 1)      # 空仓
        dp_hold = [INF] * (k + 1)       # 持有多头
        dp_short = [INF] * (k + 1)      # 持有空头

        dp_empty[0] = 0  # 初始空仓，0 笔交易完成，利润 0

        for p in prices:
            new_empty = [INF] * (k + 1)
            new_hold = [INF] * (k + 1)
            new_short = [INF] * (k + 1)

            for t in range(k + 1):
                # 空仓状态：
                # 1. 保持空仓
                # 2. 从多头卖出，完成第 t 笔交易
                # 3. 从空头买回，完成第 t 笔交易
                val = dp_empty[t]
                if t >= 1:
                    if dp_hold[t - 1] != INF:
                        val = max(val, dp_hold[t - 1] + p)  # 卖出多头
                    if dp_short[t - 1] != INF:
                        val = max(val, dp_short[t - 1] - p)  # 买回空头
                new_empty[t] = val

                # 多头持仓：
                # 1. 保持多头
                # 2. 从空仓买入（不增加已完成交易数）
                val = dp_hold[t]
                if dp_empty[t] != INF:
                    val = max(val, dp_empty[t] - p)
                new_hold[t] = val

                # 空头持仓：
                # 1. 保持空头
                # 2. 从空仓做空卖出（不增加已完成交易数）
                val = dp_short[t]
                if dp_empty[t] != INF:
                    val = max(val, dp_empty[t] + p)
                new_short[t] = val

            dp_empty = new_empty
            dp_hold = new_hold
            dp_short = new_short

        # 答案：空仓状态下，任意交易次数（≤ k）的最大利润
        ans = 0
        for t in range(k + 1):
            if dp_empty[t] > ans:
                ans = dp_empty[t]
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 使用动态规划，定义三个状态：
# - 空仓（0）：手中无任何持仓
# - 多头（1）：持有股票（买入后待卖出）
# - 空头（2）：做空持仓（卖出借来的股票后待买回）
#
# dp[t][state] 表示完成了 t 笔交易后处于 state 状态的最大利润。
# 状态转移（遍历每天的价格 p）：
# - 空仓 → 多头：买入股票，利润 -= p，交易数不变
# - 空仓 → 空头：做空卖出，利润 += p，交易数不变
# - 多头 → 空仓：卖出股票，利润 += p，交易数 +1
# - 空头 → 空仓：买回股票，利润 -= p，交易数 +1
# 每种状态也可以保持不变。
# 最终答案：空仓状态下完成 ≤ k 笔交易的最大利润。
#
# 时间复杂度: O(n * k)，其中 n 是天数
# 空间复杂度: O(k) — 只需保留前一天的状态
#
# 关键点:
# - 允许普通交易（先买后卖）和做空交易（先卖后买）两种类型
# - 交易完成以平仓为标志（卖出平多或买回平空）
# - 状态压缩：只保留三个状态的一维 dp 数组
