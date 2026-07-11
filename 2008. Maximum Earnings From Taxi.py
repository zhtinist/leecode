"""
LeetCode #2008 - Maximum Earnings From Taxi
出租车的最大盈利
https://leetcode.cn/problems/maximum-earnings-from-taxi/

你驾驶出租车行驶在一条有 `n` 个地点的路上。这 `n` 个地点从近到远编号为 `1` 到 `n` ，你想要从 `1` 开到 `n` ，通过接乘客订单盈利。你只能沿着编号递增的方向前进，不能改变方向。
乘客信息用一个下标从 0 开始的二维数组 `rides` 表示，其中 `rides[i] = [start_i, end_i, tip_i]` 表示第 `i` 位乘客需要从地点 `start_i` 前往 `end_i` ，愿意支付 `tip_i` 元的小费。
每一位 你选择接单的乘客 `i` ，你可以 盈利 `end_i - start_i + tip_i` 元。你同时 最多 只能接一个订单。
给你 `n` 和 `rides` ，请你返回在最优接单方案下，你能盈利 最多 多少元。
注意：你可以在一个地点放下一位乘客，并在同一个地点接上另一位乘客。

示例 1：
输入：n = 5, rides = [[2,5,4],[1,5,1]] 输出：7 解释：我们可以接乘客 0 的订单，获得 5 - 2 + 4 = 7 元。
示例 2：
输入：n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]] 输出：20 解释：我们可以接以下乘客的订单： - 将乘客 1 从地点 3 送往地点 10 ，获得 10 - 3 + 2 = 9 元。 - 将乘客 2 从地点 10 送往地点 12 ，获得 12 - 10 + 3 = 5 元。 - 将乘客 5 从地点 13 送往地点 18 ，获得 18 - 13 + 1 = 6 元。 我们总共获得 9 + 5 + 6 = 20 元。

提示：
`1 <= n <= 10^5`
`1 <= rides.length <= 3 * 10^4`
`rides[i].length == 3`
`1 <= start_i < end_i <= n`
`1 <= tip_i <= 10^5`
"""

from typing import List, Optional


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        """
        DP: dp[i] = max earnings at point i.
        Group rides by end point. For each ride (start, end, tip),
        profit = end - start + tip.
        """
        # Group rides by end point
        rides_by_end = [[] for _ in range(n + 1)]
        for start, end, tip in rides:
            profit = end - start + tip
            rides_by_end[end].append((start, profit))

        dp = [0] * (n + 1)  # dp[i] = max earnings up to point i

        for i in range(1, n + 1):
            # Option 1: skip point i (no pickup)
            dp[i] = dp[i - 1]
            # Option 2: take a ride ending at i
            for start, profit in rides_by_end[i]:
                dp[i] = max(dp[i], dp[start] + profit)

        return dp[n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Binary Search, Dynamic Programming, Sorting
#
# 解题思路:
# 动态规划。dp[i] = 到达位置 i 时的最大盈利。
# 按终点分组所有行程。对于每个位置 i：
# - 不在 i 接客：dp[i] = dp[i-1]
# - 接受终点在 i 的某个行程：(start, profit)：dp[i] = max(dp[i], dp[start] + profit)
# 因为行程方向只能递增（从 start 到 end），到达终点前可以从 start 接客。
#
# 时间复杂度: O(N + R)，N 为位置数，R 为行程数
# 空间复杂度: O(N + R)
#
# 关键点:
# - 一维 DP：dp[i] 表示到位置 i 的最大盈利
# - 按终点分组，转移时从起点取前置状态
# - 每个位置可以选择不接客（继承前一个状态）
