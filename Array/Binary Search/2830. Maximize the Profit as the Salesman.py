"""
LeetCode #2830 - Maximize the Profit as the Salesman
销售利润最大化
https://leetcode.cn/problems/maximize-the-profit-as-the-salesman/

给你一个整数 `n` 表示数轴上的房屋数量，编号从 `0` 到 `n - 1` 。
另给你一个二维整数数组 `offers` ，其中 `offers[i] = [start_i, end_i, gold_i]` 表示第 `i` 个买家想要以 `gold_i` 枚金币的价格购买从 `start_i` 到 `end_i` 的所有房屋。
作为一名销售，你需要有策略地选择并销售房屋使自己的收入最大化。
返回你可以赚取的金币的最大数目。
注意 同一所房屋不能卖给不同的买家，并且允许保留一些房屋不进行出售。

示例 1：
输入：n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]] 输出：3 解释： 有 5 所房屋，编号从 0 到 4 ，共有 3 个购买要约。 将位于 [0,0] 范围内的房屋以 1 金币的价格出售给第 1 位买家，并将位于 [1,3] 范围内的房屋以 2 金币的价格出售给第 3 位买家。 可以证明我们最多只能获得 3 枚金币。
示例 2：
输入：n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]] 输出：10 解释：有 5 所房屋，编号从 0 到 4 ，共有 3 个购买要约。 将位于 [0,2] 范围内的房屋以 10 金币的价格出售给第 2 位买家。 可以证明我们最多只能获得 10 枚金币。

提示：
`1 <= n <= 10^5`
`1 <= offers.length <= 10^5`
`offers[i].length == 3`
`0 <= start_i <= end_i <= n - 1`
`1 <= gold_i <= 10^3`
"""

from typing import List, Optional


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: x[1])
        m = len(offers)
        dp = [0] * (n + 1)
        j = 0
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            while j < m and offers[j][1] == i - 1:
                start, end, gold = offers[j]
                dp[i] = max(dp[i], dp[start] + gold)
                j += 1
        return dp[n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Binary Search, Dynamic Programming, Sorting
#
# 解题思路:
# 将 offers 按结束位置 end 排序。DP：dp[i] 表示前 i 个房屋（0 到 i-1）能获得的最大利润。
# 对于位置 i，有两种选择：不卖第 i-1 个房屋（dp[i] = dp[i-1]），或卖以 i-1 结尾的某个 offer（dp[i] = dp[start] + gold）。
# 按结束位置有序处理所有 offers，每次更新 dp[i] 为两种选择的最大值。
#
# 时间复杂度: O(n + m log m) 其中 m = len(offers)
# 空间复杂度: O(n)
#
# 关键点:
# - 按结束位置排序 offers，使得 DP 处理有序
# - dp[i] = max(dp[i-1], dp[start] + gold) 标准不重叠区间 DP
# - 房屋编号从 0 开始，dp 数组偏移处理
