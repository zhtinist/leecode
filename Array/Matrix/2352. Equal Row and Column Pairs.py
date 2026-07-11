"""
LeetCode #2352 - Equal Row and Column Pairs
相等行列对
https://leetcode.cn/problems/equal-row-and-column-pairs/

给你一个下标从 0 开始、大小为 `n x n` 的整数矩阵 `grid` ，返回满足 `R_i` 行和 `C_j` 列相等的行列对 `(R_i, C_j)` 的数目。
如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。

示例 1：

输入：grid = [[3,2,1],[1,7,6],[2,7,7]] 输出：1 解释：存在一对相等行列对： - (第 2 行，第 1 列)：[2,7,7]
示例 2：

输入：grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]] 输出：3 解释：存在三对相等行列对： - (第 0 行，第 0 列)：[3,1,2,2] - (第 2 行, 第 2 列)：[2,4,2,2] - (第 3 行, 第 2 列)：[2,4,2,2]

提示：
`n == grid.length == grid[i].length`
`1 <= n <= 200`
`1 <= grid[i][j] <= 10^5`
"""

from typing import List, Optional


from collections import Counter


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_counter = Counter(tuple(row) for row in grid)

        result = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            if col in row_counter:
                result += row_counter[col]
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Matrix, Simulation
#
# 解题思路:
# 用 Counter 统计每一行（转为 tuple）出现的频次。
# 然后遍历每一列（同样转为 tuple），检查该列是否在 row_counter 中出现过，
# 若出现则累加其频次到结果中（因为该列可以与所有相同的行配对）。
#
# 时间复杂度: O(N^2) 其中 N 为矩阵边长，需要遍历所有元素
# 空间复杂度: O(N^2) 存储所有行和列的元组（Counter 中最多 N 个元组，每个长度 N）
#
# 关键点:
# - 将行/列转为 tuple 使其可哈希，作为 Counter 的 key
# - 列转换：tuple(grid[i][j] for i in range(n))
# - 累加频次而非计数 1，因为每行可以匹配多次
