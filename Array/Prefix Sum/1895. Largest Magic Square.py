"""
LeetCode #1895 - Largest Magic Square
最大的幻方
https://leetcode.cn/problems/largest-magic-square/

一个 `k x k` 的 幻方 指的是一个 `k x k` 填满整数的方格阵，且每一行、每一列以及两条对角线的和 全部相等 。幻方中的整数 不需要互不相同 。显然，每个 `1 x 1` 的方格都是一个幻方。
给你一个 `m x n` 的整数矩阵 `grid` ，请你返回矩阵中 最大幻方 的 尺寸 （即边长 `k`）。

示例 1：
输入：grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]] 输出：3 解释：最大幻方尺寸为 3 。 每一行，每一列以及两条对角线的和都等于 12 。 - 每一行的和：5+1+6 = 5+4+3 = 2+7+3 = 12 - 每一列的和：5+5+2 = 1+4+7 = 6+3+3 = 12 - 对角线的和：5+4+3 = 6+4+2 = 12
示例 2：
输入：grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]] 输出：2

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 50`
`1 <= grid[i][j] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Prefix sums for rows, columns
        row_pref = [[0] * (n + 1) for _ in range(m)]
        col_pref = [[0] * (m + 1) for _ in range(n)]

        for i in range(m):
            for j in range(n):
                row_pref[i][j + 1] = row_pref[i][j] + grid[i][j]
                col_pref[j][i + 1] = col_pref[j][i] + grid[i][j]

        def row_sum(r: int, c1: int, c2: int) -> int:
            return row_pref[r][c2 + 1] - row_pref[r][c1]

        def col_sum(c: int, r1: int, r2: int) -> int:
            return col_pref[c][r2 + 1] - col_pref[c][r1]

        def diag_sum(r1: int, c1: int, r2: int, c2: int) -> int:
            # Main diagonal: top-left to bottom-right
            s = 0
            r, c = r1, c1
            while r <= r2 and c <= c2:
                s += grid[r][c]
                r += 1
                c += 1
            return s

        def anti_diag_sum(r1: int, c1: int, r2: int, c2: int) -> int:
            # Anti-diagonal: top-right to bottom-left
            s = 0
            r, c = r1, c2
            while r <= r2 and c >= c1:
                s += grid[r][c]
                r += 1
                c -= 1
            return s

        def is_magic(r: int, c: int, k: int) -> bool:
            target = row_sum(r, c, c + k - 1)
            # Check all rows
            for i in range(r, r + k):
                if row_sum(i, c, c + k - 1) != target:
                    return False
            # Check all columns
            for j in range(c, c + k):
                if col_sum(j, r, r + k - 1) != target:
                    return False
            # Check main diagonal
            if diag_sum(r, c, r + k - 1, c + k - 1) != target:
                return False
            # Check anti-diagonal
            if anti_diag_sum(r, c, r + k - 1, c + k - 1) != target:
                return False
            return True

        max_k = min(m, n)
        # Check from largest k to smallest
        for k in range(max_k, 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic(i, j, k):
                        return k

        return 1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Prefix Sum
#
# 解题思路:
# 使用前缀和优化行列求和，从大到小枚举幻方尺寸。
# 1. 构建行前缀和和列前缀和数组，O(1) 查询任意行/列的区间和。
# 2. 从最大的可能尺寸 k = min(m, n) 向下枚举，
#    对每个可能的左上角位置检查是否为幻方。
# 3. 检查条件：所有行和、列和、两条对角线和相等。
# 4. 找到的第一个（最大的 k）即为答案。
#
# 时间复杂度: O(m * n * min(m, n)^2) — 枚举所有子矩阵
# 空间复杂度: O(m * n) — 前缀和数组
#
# 关键点:
# - 从大到小搜索，提前返回
# - 行和列使用前缀和 O(1) 计算
# - 对角线需要逐个累加（因为不是规则的直线段）
# - 1x1 的幻方总是有效的
