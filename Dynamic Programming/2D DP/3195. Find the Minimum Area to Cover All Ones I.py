"""
LeetCode #3195 - Find the Minimum Area to Cover All Ones I
包含所有 1 的最小矩形面积 I
https://leetcode.cn/problems/find-the-minimum-area-to-cover-all-ones-i/

给你一个二维 二进制 数组 `grid`。请你找出一个边在水平方向和竖直方向上、面积 最小 的矩形，并且满足 `grid` 中所有的 1 都在矩形的内部。
返回这个矩形可能的 最小 面积。

示例 1：

输入： grid = [[0,1,0],[1,0,1]]
输出： 6
解释：

这个最小矩形的高度为 2，宽度为 3，因此面积为 `2 * 3 = 6`。
示例 2：

输入： grid = [[0,0],[1,0]]
输出： 1
解释：

这个最小矩形的高度和宽度都是 1，因此面积为 `1 * 1 = 1`。

提示：
`1 <= grid.length, grid[i].length <= 1000`
`grid[i][j]` 是 0 或 1。
输入保证 `grid` 中至少有一个 1 。
"""

from typing import List, Optional


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_r, max_r = m, -1
        min_c, max_c = n, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_r = min(min_r, i)
                    max_r = max(max_r, i)
                    min_c = min(min_c, j)
                    max_c = max(max_c, j)

        return (max_r - min_r + 1) * (max_c - min_c + 1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix
#
# 解题思路:
# 最小矩形面积由1的边界决定：找到所有1的最小/最大行索引和列索引。
# 矩形的宽 = max_col - min_col + 1，高 = max_row - min_row + 1。
# 面积 = 宽 * 高。题目保证至少有一个1。
#
# 时间复杂度: O(m*n)
# 空间复杂度: O(1)
#
# 关键点:
# - 矩形的边界由最外层的1决定
# - 记录四个方向的极值
# - 面积 = (max-min+1)相乘
