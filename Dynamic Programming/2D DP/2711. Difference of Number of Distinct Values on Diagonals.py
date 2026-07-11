"""
LeetCode #2711 - Difference of Number of Distinct Values on Diagonals
对角线上不同值的数量差
https://leetcode.cn/problems/difference-of-number-of-distinct-values-on-diagonals/

给你一个下标从 `0` 开始、大小为 `m x n` 的二维矩阵 `grid` ，请你求解大小同样为 `m x n` 的答案矩阵 `answer` 。
矩阵 `answer` 中每个单元格 `(r, c)` 的值可以按下述方式进行计算：
令 `topLeft[r][c]` 为矩阵 `grid` 中单元格 `(r, c)` 左上角对角线上 不同值 的数量。
令 `bottomRight[r][c]` 为矩阵 `grid` 中单元格 `(r, c)` 右下角对角线上 不同值 的数量。
然后 `answer[r][c] = |topLeft[r][c] - bottomRight[r][c]|` 。
返回矩阵 `answer` 。
矩阵对角线 是从最顶行或最左列的某个单元格开始，向右下方向走到矩阵末尾的对角线。
如果单元格 `(r1, c1)` 和单元格 `(r, c) `属于同一条对角线且 `r1 < r` ，则单元格 `(r1, c1)` 属于单元格 `(r, c)` 的左上对角线。类似地，可以定义右下对角线。

示例 1：
输入：grid = [[1,2,3],[3,1,5],[3,2,1]] 输出：[[1,1,0],[1,0,1],[0,1,1]] 解释：第 1 个图表示最初的矩阵 grid 。  第 2 个图表示对单元格 (0,0) 计算，其中蓝色单元格是位于右下对角线的单元格。 第 3 个图表示对单元格 (1,2) 计算，其中红色单元格是位于左上对角线的单元格。 第 4 个图表示对单元格 (1,1) 计算，其中蓝色单元格是位于右下对角线的单元格，红色单元格是位于左上对角线的单元格。 - 单元格 (0,0) 的右下对角线包含 [1,1] ，而左上对角线包含 [] 。对应答案是 |1 - 0| = 1 。 - 单元格 (1,2) 的右下对角线包含 [] ，而左上对角线包含 [2] 。对应答案是 |0 - 1| = 1 。 - 单元格 (1,1) 的右下对角线包含 [1] ，而左上对角线包含 [1] 。对应答案是 |1 - 1| = 0 。 其他单元格的对应答案也可以按照这样的流程进行计算。
示例 2：
输入：grid = [[1]] 输出：[[0]] 解释：- 单元格 (0,0) 的右下对角线包含 [] ，左上对角线包含 [] 。对应答案是 |0 - 0| = 0 。

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n, grid[i][j] <= 50`
"""

from typing import List, Optional


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]

        # top-left to bottom-right: for each diagonal
        # For each cell, topLeft[r][c] = distinct values from grid[r-1][c-1], grid[r-2][c-2], ...
        # bottomRight[r][c] = distinct values from grid[r+1][c+1], grid[r+2][c+2], ...

        # Process diagonals: for each starting cell on top row and left column
        for d in range(-(m - 1), n):
            # r - c = d
            r_start = max(0, d)
            c_start = max(0, -d)

            # First pass: compute topLeft (distinct values in prefix of this diagonal)
            seen = set()
            top_left = {}
            r, c = r_start, c_start
            while r < m and c < n:
                top_left[(r, c)] = len(seen)
                seen.add(grid[r][c])
                r += 1
                c += 1

            # Second pass: compute bottomRight (distinct values in suffix of this diagonal)
            # Go backwards to compute suffix distinct counts
            seen = set()
            bottom_right = {}
            # Collect all cells in this diagonal
            cells = []
            r, c = r_start, c_start
            while r < m and c < n:
                cells.append((r, c))
                r += 1
                c += 1

            for r, c in reversed(cells):
                seen.add(grid[r][c])
                bottom_right[(r, c)] = len(seen)

            # Compute answer for each cell in this diagonal
            for i, (r, c) in enumerate(cells):
                # topLeft excludes current cell
                tl = top_left[(r, c)]
                # bottomRight: after current cell, so exclude current from suffix
                # Actually: bottomRight should be distinct AFTER current cell
                # So we need suffix excluding current
                if i + 1 < len(cells):
                    br_cell = cells[i + 1]
                    br = bottom_right[br_cell]
                else:
                    br = 0
                ans[r][c] = abs(tl - br)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Matrix
#
# 解题思路:
# 按对角线（从左上到右下）处理。对于每条对角线，先正向遍历计算每个位置左上对角线的不同值数量
# （用集合累加沿途元素）。再反向遍历计算右下角不同值数量。每个单元格的答案为两者差的绝对值。
# 注意topLeft不包括当前元素，bottomRight也不包括当前元素。
#
# 时间复杂度: O(m * n)
# 空间复杂度: O(m * n)
#
# 关键点:
# - 按对角线处理，每条对角线独立计算
# - 正向扫描计算前缀不同值，反向扫描计算后缀不同值
# - topLeft取当前元素之前的集合大小，bottomRight取当前元素之后的集合大小
