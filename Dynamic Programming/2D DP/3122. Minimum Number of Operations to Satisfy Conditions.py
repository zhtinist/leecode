"""
LeetCode #3122 - Minimum Number of Operations to Satisfy Conditions
使矩阵满足条件的最少操作次数
https://leetcode.cn/problems/minimum-number-of-operations-to-satisfy-conditions/

给你一个大小为 `m x n` 的二维矩形 `grid` 。每次 操作 中，你可以将 任一 格子的值修改为 任意 非负整数。完成所有操作后，你需要确保每个格子 `grid[i][j]` 的值满足：
如果下面相邻格子存在的话，它们的值相等，也就是 `grid[i][j] == grid[i + 1][j]`（如果存在）。
如果右边相邻格子存在的话，它们的值不相等，也就是 `grid[i][j] != grid[i][j + 1]`（如果存在）。
请你返回需要的 最少 操作数目。

示例 1：

输入：grid = [[1,0,2],[1,0,2]]
输出：0
解释：

矩阵中所有格子已经满足要求。
示例 2：

输入：grid = [[1,1,1],[0,0,0]]
输出：3
解释：

将矩阵变成 `[[1,0,1],[1,0,1]]` ，它满足所有要求，需要 3 次操作：
将 `grid[1][0]` 变为 1 。
将 `grid[0][1]` 变为 0 。
将 `grid[1][2]` 变为 1 。
示例 3：

输入：grid = [[1],[2],[3]]
输出：2
解释：

这个矩阵只有一列，我们可以通过 2 次操作将所有格子里的值变为 1 。

提示：
`1 <= n, m <= 1000`
`0 <= grid[i][j] <= 9`
"""

from typing import List, Optional


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # count[j][v] = 第j列中值为v的单元格数量
        count = [[0] * 10 for _ in range(n)]
        for j in range(n):
            for i in range(m):
                count[j][grid[i][j]] += 1

        dp = [0] * 10  # dp[v] = 当前列选值为v时的最小操作数
        for j in range(n):
            new_dp = [float('inf')] * 10
            for v in range(10):
                cost_v = m - count[j][v]  # 将第j列全部变成v的代价
                if j == 0:
                    new_dp[v] = cost_v
                else:
                    # 前一列的值u必须与v不同
                    min_prev = min(dp[u] for u in range(10) if u != v)
                    new_dp[v] = cost_v + min_prev
            dp = new_dp

        return min(dp)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Matrix
#
# 解题思路:
# 条件1要求同一列所有值相同；条件2要求相邻列值不同。值域只有0-9。
# 动态规划：dp[j][v]表示前j列满足条件且第j列值为v的最小操作数。
# 转移方程：dp[j][v] = cost(j,v) + min(dp[j-1][u] for u != v)。
# cost(j,v)为将第j列全部变为v的操作数 = 该列总行数 - 该列已有v的个数。
#
# 时间复杂度: O(n * 10 * 10) = O(100n)
# 空间复杂度: O(10) = O(1)（dp滚动数组）
#
# 关键点:
# - 值域只有0-9，使DP可行
# - 每列只选一个值，代价为该列中非该值的数量
# - 相邻列约束转化为DP转移时排除相同值
