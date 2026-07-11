"""
LeetCode #256 - Paint House
中文题名：粉刷房子
https://leetcode.com/problems/paint-house/

There are a row of *n* houses, each house can be painted with one of the three colors:
red, blue or green. The cost of painting each house with a certain color is different. You
have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a `*n* x *3*`
cost matrix. For example, `costs[0][0]` is the cost of painting house 0 with
color red; `costs[1][2]` is the cost of painting house 1 with color green, and so
on... Find the minimum cost to paint all houses.

Note:

All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

【中文翻译】
有一排 *n* 个房子，每个房子可以被涂成红色、蓝色或绿色这三种颜色之一。用某种颜色粉刷每个房子都有不同的花费。你必须粉刷所有的房子，且相邻的两座房子颜色不能相同。

用 `*n* x *3*` 的成本矩阵表示粉刷每个房子某种颜色的花费。例如，`costs[0][0]` 是粉刷 0 号房子为红色的花费；`costs[1][2]` 是粉刷 1 号房子为绿色的花费，以此类推……找出粉刷所有房子的最低花费。

注意：

所有花费均为正整数。

示例：

输入：[[17,2,17],[16,16,5],[14,3,19]]
输出：10
解释：将 0 号房子刷成蓝色，1 号房子刷成绿色，2 号房子刷成蓝色。
最低花费：2 + 5 + 3 = 10。
"""

from typing import List, Optional


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n = len(costs)
        # dp[i][c] = 粉刷前 i+1 个房子，且第 i 个房子颜色为 c 的最小花费
        # 直接原地修改 costs 以节省空间
        for i in range(1, n):
            # 第 i 个房子刷红色：前一个房子只能刷蓝色或绿色
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            # 第 i 个房子刷蓝色：前一个房子只能刷红色或绿色
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            # 第 i 个房子刷绿色：前一个房子只能刷红色或蓝色
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[-1])


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 动态规划。对于第 i 个房子刷每种颜色，最小花费等于该颜色花费加上
# 前一个房子刷另外两种颜色中的最小花费。状态转移：
# dp[i][红] = cost[i][红] + min(dp[i-1][蓝], dp[i-1][绿])
# 同理处理蓝色和绿色。最终答案是最后一行的最小值。
# 原地修改 costs 数组实现 O(1) 额外空间。
#
# 时间复杂度: O(n) — 遍历一次 houses
# 空间复杂度: O(1) — 原地修改
#
# 关键点：
# - 相邻房子不能同色，所以选前一个的另外两种颜色中花费最小的
# - 原地 DP 节省空间
# - 注意边界：空数组返回 0
