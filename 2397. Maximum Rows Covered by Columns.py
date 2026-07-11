"""
LeetCode #2397 - Maximum Rows Covered by Columns
被列覆盖的最多行数
https://leetcode.cn/problems/maximum-rows-covered-by-columns/

给你一个下标从 0 开始、大小为 `m x n` 的二进制矩阵 `matrix` ；另给你一个整数 `numSelect`，表示你必须从 `matrix` 中选择的 不同 列的数量。
如果一行中所有的 `1` 都被你选中的列所覆盖，则认为这一行被 覆盖 了。
形式上，假设 `s = {c_1, c_2, ...., c_numSelect}` 是你选择的列的集合。对于矩阵中的某一行 `row` ，如果满足下述条件，则认为这一行被集合 `s` 覆盖：
对于满足 `matrix[row][col] == 1` 的每个单元格 `matrix[row][col]`（`0 <= col <= n - 1`），`col` 均存在于 `s` 中，或者
`row` 中 不存在 值为 `1` 的单元格。
你需要从矩阵中选出 `numSelect` 个列，使集合覆盖的行数最大化。
返回一个整数，表示可以由 `numSelect` 列构成的集合 覆盖 的 最大行数 。

示例 1：

输入：matrix = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], numSelect = 2 输出：3 解释： 图示中显示了一种覆盖 3 行的可行办法。 选择 s = {0, 2} 。 - 第 0 行被覆盖，因为其中没有出现 1 。 - 第 1 行被覆盖，因为值为 1 的两列（即 0 和 2）均存在于 s 中。 - 第 2 行未被覆盖，因为 matrix[2][1] == 1 但是 1 未存在于 s 中。 - 第 3 行被覆盖，因为 matrix[2][2] == 1 且 2 存在于 s 中。 因此，可以覆盖 3 行。 另外 s = {1, 2} 也可以覆盖 3 行，但可以证明无法覆盖更多行。
示例 2：

输入：matrix = [[1],[0]], numSelect = 1 输出：2 解释： 选择唯一的一列，两行都被覆盖了，因为整个矩阵都被覆盖了。 所以我们返回 2 。

提示：
`m == matrix.length`
`n == matrix[i].length`
`1 <= m, n <= 12`
`matrix[i][j]` 要么是 `0` 要么是 `1`
`1 <= numSelect <= n`
"""

from typing import List, Optional


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        """
        Enumerate all combinations of selecting numSelect columns
        using bitmask. For each column mask, count how many rows
        are fully covered (all 1s in that row fall within selected columns).
        """
        from itertools import combinations

        m, n = len(matrix), len(matrix[0])

        # Precompute row masks: for each row, which columns have a 1
        row_masks = []
        for row in matrix:
            mask = 0
            for j, val in enumerate(row):
                if val == 1:
                    mask |= (1 << j)
            row_masks.append(mask)

        max_covered = 0

        # Generate all combinations of numSelect columns
        for cols in combinations(range(n), numSelect):
            col_mask = 0
            for c in cols:
                col_mask |= (1 << c)

            covered = 0
            for row_mask in row_masks:
                # A row is covered if every 1 in the row is in selected columns:
                # (row_mask & col_mask) == row_mask
                if (row_mask & col_mask) == row_mask:
                    covered += 1

            max_covered = max(max_covered, covered)

        return max_covered



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Backtracking, Enumeration, Matrix
#
# 解题思路:
# 1. 将每行转换为位掩码：如果 matrix[i][j] == 1，则第 j 位为 1。
# 2. 枚举所有从 n 列中选择 numSelect 列的组合（使用 itertools.combinations）。
# 3. 对于每种列选择，检查每一行是否被覆盖：若 row_mask & col_mask == row_mask，则该行所有 1 的列都在选中列中，该行被覆盖。
# 4. 记录最大的覆盖行数。
#
# 时间复杂度: O(C(n, numSelect) * m) — 枚举组合数 * 行数。由于 m, n <= 12，完全可行
# 空间复杂度: O(m) — 存储行掩码
#
# 关键点:
# - 位掩码大幅简化了"检查行是否被列集合覆盖"的操作
# - n <= 12 使得组合枚举完全可行（最坏 C(12,6)=924 种组合）
# - 注意：全零行始终被覆盖（row_mask=0，任何 col_mask 都满足条件）
