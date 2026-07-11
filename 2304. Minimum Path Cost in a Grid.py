"""
LeetCode #2304 - Minimum Path Cost in a Grid
网格中的最小路径代价
https://leetcode.cn/problems/minimum-path-cost-in-a-grid/

给你一个下标从 0 开始的整数矩阵 `grid` ，矩阵大小为 `m x n` ，由从 `0` 到 `m * n - 1` 的不同整数组成。你可以在此矩阵中，从一个单元格移动到 下一行 的任何其他单元格。如果你位于单元格 `(x, y)` ，且满足 `x < m - 1` ，你可以移动到 `(x + 1, 0)`, `(x + 1, 1)`, ..., `(x + 1, n - 1)` 中的任何一个单元格。注意： 在最后一行中的单元格不能触发移动。
每次可能的移动都需要付出对应的代价，代价用一个下标从 0 开始的二维数组 `moveCost` 表示，该数组大小为 `(m * n) x n` ，其中 `moveCost[i][j]` 是从值为 `i` 的单元格移动到下一行第 `j` 列单元格的代价。从 `grid` 最后一行的单元格移动的代价可以忽略。
`grid` 一条路径的代价是：所有路径经过的单元格的 值之和 加上 所有移动的 代价之和 。从 第一行 任意单元格出发，返回到达 最后一行 任意单元格的最小路径代价。

示例 1：

输入：grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]] 输出：17 解释：最小代价的路径是 5 -> 0 -> 1 。 - 路径途经单元格值之和 5 + 0 + 1 = 6 。 - 从 5 移动到 0 的代价为 3 。 - 从 0 移动到 1 的代价为 8 。 路径总代价为 6 + 3 + 8 = 17 。
示例 2：
输入：grid = [[5,1,2],[4,0,3]], moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]] 输出：6 解释： 最小路径的路径是 2 -> 3 。  - 路径途经单元格值之和 2 + 3 = 5 。  - 从 2 移动到 3 的代价为 1 。  路径总代价为 5 + 1 = 6 。

提示：
`m == grid.length`
`n == grid[i].length`
`2 <= m, n <= 50`
`grid` 由从 `0` 到 `m * n - 1` 的不同整数组成
`moveCost.length == m * n`
`moveCost[i].length == n`
`1 <= moveCost[i][j] <= 100`
"""

from typing import List, Optional


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[row][col] 表示从第一行某个单元格出发，到达 (row, col) 的最小路径代价
        # 初始化第一行：从第一行任意单元格出发，初始代价就是该单元格的值
        dp = [[0] * n for _ in range(m)]
        for c in range(n):
            dp[0][c] = grid[0][c]

        # 逐行计算
        for r in range(1, m):
            for c in range(n):
                # 计算到达 (r, c) 的最小代价
                # 从上一行的每个列 j 转移到当前列 c
                min_cost = float('inf')
                for j in range(n):
                    # dp[r-1][j] + moveCost[grid[r-1][j]][c] + grid[r][c]
                    cost = dp[r - 1][j] + moveCost[grid[r - 1][j]][c] + grid[r][c]
                    if cost < min_cost:
                        min_cost = cost
                dp[r][c] = min_cost

        # 返回到达最后一行的最小代价
        return min(dp[m - 1])


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Matrix
#
# 解题思路:
# 使用二维动态规划。定义 dp[r][c] 表示从第一行某个单元格出发，到达 (r, c) 的最小路径代价。
#
# 1. 初始化：第一行 dp[0][c] = grid[0][c]（起点代价就是单元格值本身）
#
# 2. 状态转移：对于第 r 行 (r >= 1) 的每个单元格 (r, c)：
#    dp[r][c] = min over j in [0, n-1] {
#        dp[r-1][j] + moveCost[grid[r-1][j]][c] + grid[r][c]
#    }
#    即从上一行的每一列 j 都可以转移到当前列 c，选择总代价最小的路径。
#    其中 moveCost 的索引是"上一行单元格的值"而非列号，因为相同值在不同行可能有不同的移动代价，
#    这正是通过单元格的值来索引 moveCost 的原因。
#
# 3. 最终答案：min(dp[m-1][c]) for all c，即到达最后一行的最小代价。
#
# 时间复杂度: O(m * n^2)
# - 共 m 行 n 列，每格需要遍历上一行的 n 个列来取最小值
#
# 空间复杂度: O(m * n)
# - dp 数组大小 m x n。可以优化为 O(n)，只保留上一行和当前行
#
# 关键点:
# - moveCost 的索引是单元格的值（grid[r-1][j]），不是列号
# - 路径代价 = 经过的单元格值之和 + 移动代价之和，两者都计入 dp
# - 从第一行的任意列出发，到最后一行的任意列结束
