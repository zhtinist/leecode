"""
LeetCode #2684 - Maximum Number of Moves in a Grid
矩阵中移动的最大次数
https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/

给你一个下标从 0 开始、大小为 `m x n` 的矩阵 `grid` ，矩阵由若干 正 整数组成。
你可以从矩阵第一列中的 任一 单元格出发，按以下方式遍历 `grid` ：
从单元格 `(row, col)` 可以移动到 `(row - 1, col + 1)`、`(row, col + 1)` 和 `(row + 1, col + 1)` 三个单元格中任一满足值 严格 大于当前单元格的单元格。
返回你在矩阵中能够 移动 的 最大 次数。

示例 1：
输入：grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]] 输出：3 解释：可以从单元格 (0, 0) 开始并且按下面的路径移动： - (0, 0) -> (0, 1). - (0, 1) -> (1, 2). - (1, 2) -> (2, 3). 可以证明这是能够移动的最大次数。
示例 2：
输入：grid = [[3,2,4],[2,1,9],[1,1,7]] 输出：0 解释：从第一列的任一单元格开始都无法移动。

提示：
`m == grid.length`
`n == grid[i].length`
`2 <= m, n <= 1000`
`4 <= m * n <= 10^5`
`1 <= grid[i][j] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[r] = max column reachable from first column ending at row r in current column
        # Actually simpler: track which rows are reachable in current column
        reachable = set(range(m))  # all rows in column 0 are startable
        ans = 0

        for j in range(1, n):
            next_reachable = set()
            for r in reachable:
                for nr in (r - 1, r, r + 1):
                    if 0 <= nr < m and grid[nr][j] > grid[r][j - 1]:
                        next_reachable.add(nr)
            if not next_reachable:
                break
            reachable = next_reachable
            ans = j

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Matrix
#
# 解题思路:
# 逐列BFS/DP。从第一列所有行出发，每列维护当前可达的行集合。
# 对于下一列，检查每个可达行的三个方向(右上、右、右下)是否能移动到值更大的格子。
# 移动次数等于能到达的最远列号。当无法前进时停止。
#
# 时间复杂度: O(m * n)
# 空间复杂度: O(m)
#
# 关键点:
# - 每步只能向右移动，所以按列推进
# - 每次移动需要目标值严格大于当前值
# - 答案为能到达的最远列号（从第0列出发到达第j列需要j次移动）
