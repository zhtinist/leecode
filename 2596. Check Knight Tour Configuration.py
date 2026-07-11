"""
LeetCode #2596 - Check Knight Tour Configuration
检查骑士巡视方案
https://leetcode.cn/problems/check-knight-tour-configuration/

骑士在一张 `n x n` 的棋盘上巡视。在 有效 的巡视方案中，骑士会从棋盘的 左上角 出发，并且访问棋盘上的每个格子 恰好一次 。
给你一个 `n x n` 的整数矩阵 `grid` ，由范围 `[0, n * n - 1]` 内的不同整数组成，其中 `grid[row][col]` 表示单元格 `(row, col)` 是骑士访问的第 `grid[row][col]` 个单元格。骑士的行动是从下标 0 开始的。
如果 `grid` 表示了骑士的有效巡视方案，返回 `true`；否则返回 `false`。
注意，骑士行动时可以垂直移动两个格子且水平移动一个格子，或水平移动两个格子且垂直移动一个格子。下图展示了骑士从某个格子出发可能的八种行动路线。

示例 1：
输入：grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]] 输出：true 解释：grid 如上图所示，可以证明这是一个有效的巡视方案。
示例 2：
输入：grid = [[0,3,6],[5,8,1],[2,7,4]] 输出：false 解释：grid 如上图所示，考虑到骑士第 7 次行动后的位置，第 8 次行动是无效的。

提示：
`n == grid.length == grid[i].length`
`3 <= n <= 7`
`0 <= grid[row][col] < n * n`
`grid` 中的所有整数 互不相同
"""

from typing import List, Optional


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        if grid[0][0] != 0:
            return False
        # Map step number -> (row, col)
        pos = [None] * (n * n)
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = (i, j)

        for step in range(1, n * n):
            r1, c1 = pos[step - 1]
            r2, c2 = pos[step]
            dr, dc = abs(r1 - r2), abs(c1 - c2)
            if not ((dr == 2 and dc == 1) or (dr == 1 and dc == 2)):
                return False
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Array, Matrix, Simulation
#
# 解题思路:
# 首先检查起点是否为(0,0)（grid[0][0]==0）。然后建立步骤号到坐标的映射数组，
# 遍历每个步骤1到n*n-1，检查前后两步之间是否为合法的骑士移动：
# 骑士移动必须是(2步垂直+1步水平)或(1步垂直+2步水平)。
#
# 时间复杂度: O(N^2)
# 空间复杂度: O(N^2)
#
# 关键点:
# - 骑士移动的8个方向可简化为(dx=1,dy=2)或(dx=2,dy=1)的绝对值判断
# - 映射数组将O(N^2)的查找变为O(1)
# - 起点必须是(0,0)
