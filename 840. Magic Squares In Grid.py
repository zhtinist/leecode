"""
LeetCode #840 - Magic Squares In Grid
中文题名：矩阵中的幻方
https://leetcode.com/problems/magic-squares-in-grid/

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to
9 such that each row, column, and both diagonals all have the same sum.

Given an `grid` of integers, how many 3 x 3 "magic square" subgrids
are there?  (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
[9,5,1,9],
[2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.

Note:

`1 <= grid.length <= 10`

`1 <= grid[0].length <= 10`

`0 <= grid[i][j] <= 15`

【中文翻译】
3 x 3 的幻方是一个 3 x 3 的矩阵，其中填有 1 到 9 的不同数字，使得每一行、每一列以及两条对角线上的数字之和都相等。

给定一个 `grid` 整数矩阵，其中有多少个 3 x 3 的"幻方"子网格？（每个子网格是连续的）。

示例 1：

输入：[[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]]
输出：1
解释：
下面的子网格是一个 3 x 3 的幻方：
438
951
276

而这个不是：
384
519
762

总的来说，给定的网格内只有一个幻方。

注意：

`1 <= grid.length <= 10`

`1 <= grid[0].length <= 10`

`0 <= grid[i][j] <= 15`

"""

from typing import List, Optional


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def is_magic(r: int, c: int) -> bool:
            # Extract the 3x3 subgrid
            vals = [grid[r + i][c + j] for i in range(3) for j in range(3)]

            # Must contain distinct numbers 1-9
            if sorted(vals) != list(range(1, 10)):
                return False

            # Center must be 5 (for any 3x3 magic square using 1-9)
            if grid[r + 1][c + 1] != 5:
                return False

            # Quick sum check: each row, col, diagonal must sum to 15
            # Rows
            if grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15:
                return False
            if grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15:
                return False
            if grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15:
                return False
            # Columns
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15:
                return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15:
                return False
            # Diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False

            return True

        count = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 遍历每个可能的 3x3 子网格，检查是否为幻方。
# 3x3 幻方（使用 1-9）的已知性质：
# 1. 必须包含 1-9 所有数字各一次
# 2. 中心必须是 5
# 3. 各行、各列、两对角线之和必须为 15
# 利用这些性质可以快速筛选：
# - 先检查中心是否为 5（O(1)）
# - 检查数字是否为 1-9（可以用排序或集合）
# - 检查 8 条线（3行+3列+2对角线）的和是否都为 15
#
# 时间复杂度: O(R * C) — R、C 为网格的行数和列数，每个子网格检查 O(1)
# 空间复杂度: O(1) — 只使用常数额外空间
#
# 关键点:
# - 3x3 幻方的数学性质：中心必须是 5，每行/列/对角线和为 15
# - 数字必须恰好是 1-9（不能有重复或缺失）
# - 网格很小（<= 10x10），直接遍历所有子网格即可
# - 可以使用预定义的幻方模式进一步优化，但输入规模小所以不需要
