"""
LeetCode #3071 - Minimum Operations to Write the Letter Y on a Grid
在矩阵上写出字母 Y 所需的最少操作次数
https://leetcode.cn/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

给你一个下标从 0 开始、大小为 `n x n` 的矩阵 `grid` ，其中 `n` 为奇数，且 `grid[r][c]` 的值为 `0` 、`1` 或 `2` 。
如果一个单元格属于以下三条线中的任一一条，我们就认为它是字母 Y 的一部分：
从左上角单元格开始到矩阵中心单元格结束的对角线。
从右上角单元格开始到矩阵中心单元格结束的对角线。
从中心单元格开始到矩阵底部边界结束的垂直线。
当且仅当满足以下全部条件时，可以判定矩阵上写有字母 Y ：
属于 Y 的所有单元格的值相等。
不属于 Y 的所有单元格的值相等。
属于 Y 的单元格的值与不属于Y的单元格的值不同。
每次操作你可以将任意单元格的值改变为 `0` 、`1` 或 `2` 。返回在矩阵上写出字母 Y 所需的 最少 操作次数。

示例 1：
输入：grid = [[1,2,2],[1,1,0],[0,1,0]] 输出：3 解释：将在矩阵上写出字母 Y 需要执行的操作用蓝色高亮显示。操作后，所有属于 Y 的单元格（加粗显示）的值都为 1 ，而不属于 Y 的单元格的值都为 0 。 可以证明，写出 Y 至少需要进行 3 次操作。
示例 2：
输入：grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]] 输出：12 解释：将在矩阵上写出字母 Y 需要执行的操作用蓝色高亮显示。操作后，所有属于 Y 的单元格（加粗显示）的值都为 0 ，而不属于 Y 的单元格的值都为 2 。 可以证明，写出 Y 至少需要进行 12 次操作。

提示：
`3 <= n <= 49`
`n == grid.length == grid[i].length`
`0 <= grid[i][j] <= 2`
`n` 为奇数。
"""

from typing import List, Optional


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        """
        Identify Y cells: main diagonal, anti-diagonal to center,
        vertical from center to bottom. Count value frequencies
        in Y and non-Y cells. Try all 6 valid (y_val, other_val) pairs.
        """
        n = len(grid)
        center = n // 2

        y_count = [0, 0, 0]  # count of 0, 1, 2 in Y cells
        other_count = [0, 0, 0]  # count of 0, 1, 2 in non-Y cells

        # Mark which cells belong to Y
        is_y = [[False] * n for _ in range(n)]

        # Main diagonal: (0,0) to center
        for i in range(center + 1):
            is_y[i][i] = True
        # Anti-diagonal: (0, n-1) to center
        for i in range(center + 1):
            is_y[i][n - 1 - i] = True
        # Vertical from center to bottom
        for i in range(center, n):
            is_y[i][center] = True

        # Count
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                if is_y[i][j]:
                    y_count[val] += 1
                else:
                    other_count[val] += 1

        total_y = sum(y_count)
        total_other = n * n - total_y
        ans = float('inf')

        for y_val in range(3):
            for other_val in range(3):
                if y_val == other_val:
                    continue
                # Operations = (Y cells not y_val) + (non-Y cells not other_val)
                ops = (total_y - y_count[y_val]) + (total_other - other_count[other_val])
                ans = min(ans, ops)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Counting, Matrix
#
# 解题思路:
# 首先标记矩阵中属于字母 Y 的单元格：主对角线 (0,0) 到中心、反对角线 (0,n-1) 到中心、
# 以及从中心到底部的垂直线。统计 Y 区域和非 Y 区域中 0、1、2 的出现次数。
# 枚举 Y 区域的目标值和剩余区域的目标值（共 3*2=6 种组合，两值不同），
# 计算使两部分分别统一为该值所需的最少操作次数（即不相等的单元格数）。
#
# 时间复杂度: O(n^2)，标记和统计
# 空间复杂度: O(n^2)，标记矩阵
#
# 关键点:
# - 明确 Y 的组成部分：主对角线 + 反对角线（均到中心） + 中心垂直线
# - Y 和 非 Y 的目标值必须不同
# - 最少操作 = (Y中非目标值的数量) + (非Y中非目标值的数量)
