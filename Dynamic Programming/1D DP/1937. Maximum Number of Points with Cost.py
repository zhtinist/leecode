"""
LeetCode #1937 - Maximum Number of Points with Cost
扣分后的最大得分
https://leetcode.cn/problems/maximum-number-of-points-with-cost/

给你一个 `m x n` 的整数矩阵 `points` （下标从 0 开始）。一开始你的得分为 `0` ，你想最大化从矩阵中得到的分数。
你的得分方式为：每一行 中选取一个格子，选中坐标为 `(r, c)` 的格子会给你的总得分 增加 `points[r][c]` 。
然而，相邻行之间被选中的格子如果隔得太远，你会失去一些得分。对于相邻行 `r` 和 `r + 1` （其中 `0 = 0` ，那么值为 `x` 。
如果 `x < 0` ，那么值为 `-x` 。

示例 1：
输入：points = [[1,2,3],[1,5,1],[3,1,1]] 输出：9 解释： 蓝色格子是最优方案选中的格子，坐标分别为 (0, 2)，(1, 1) 和 (2, 0) 。 你的总得分增加 3 + 5 + 3 = 11 。 但是你的总得分需要扣除 abs(2 - 1) + abs(1 - 0) = 2 。 你的最终得分为 11 - 2 = 9 。
示例 2：
输入：points = [[1,5],[2,3],[4,2]] 输出：11 解释： 蓝色格子是最优方案选中的格子，坐标分别为 (0, 1)，(1, 1) 和 (2, 0) 。 你的总得分增加 5 + 3 + 4 = 12 。 但是你的总得分需要扣除 abs(1 - 1) + abs(1 - 0) = 1 。 你的最终得分为 12 - 1 = 11 。

提示：
`m == points.length`
`n == points[r].length`
`1 <= m, n <= 10^5`
`1 <= m * n <= 10^5`
`0 <= points[r][c] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        DP: for each row, compute max score ending at each column.
        Use left-to-right and right-to-left sweeps to handle abs(c1 - c2) penalty.
        """
        m, n = len(points), len(points[0])
        dp = points[0][:]  # dp[j] = max score ending at column j of current row

        for r in range(1, m):
            # left-to-right sweep: best from left side
            left = [0] * n
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(left[c - 1] - 1, dp[c])

            # right-to-left sweep: best from right side
            right = [0] * n
            right[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, dp[c])

            # combine: dp[j] = points[r][j] + max(left[j], right[j])
            for c in range(n):
                dp[c] = points[r][c] + max(left[c], right[c])

        return max(dp)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Matrix
#
# 解题思路:
# 定义 dp[j] = 选择当前行第 j 列时的最大累积得分。
# 从上一行转移到当前行时，需要考虑列间距的惩罚 abs(c1 - c2)。
# 朴素转移 O(n^2) 会超时。优化方法：对上一行的 dp 值分别进行从左到右和从右到左
# 的扫描，预处理出"来自左侧"和"来自右侧"的最大值。
# left[j] = max(dp[j], left[j-1] - 1)：表示从左侧某列过来，每移动一列减1。
# right[j] = max(dp[j], right[j+1] - 1)：表示从右侧某列过来。
# 最终 dp[j] = points[r][j] + max(left[j], right[j])。
#
# 时间复杂度: O(M * N)，每行扫描三次
# 空间复杂度: O(N)，只保留当前行的 dp 和临时数组
#
# 关键点:
# - 利用 left-right 扫描将 O(N^2) 优化为 O(N)
# - left[j] = max(dp[j], left[j-1] - 1) 的递推含义
# - 最后取 max(dp) 而非 dp[-1]
