"""
LeetCode #1254 - Number of Closed Islands
中文题名：统计封闭岛屿的数目
https://leetcode.com/problems/number-of-closed-islands/

Given a 2D `grid` consists of `0s` (land) and `1s`
(water).  An island is a maximal 4-directionally connected group of
`0s` and a closed island is an island
totally (all left, top, right, bottom) surrounded by `1s.`

Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
[1,0,0,0,0,0,1],
[1,0,1,1,1,0,1],
[1,0,1,0,1,0,1],
[1,0,1,1,1,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1]]
Output: 2

Constraints:

`1 <= grid.length, grid[0].length <= 100`

`0 <= grid[i][j] <=1`

【中文翻译】
给定一个二维网格 `grid`，由 `0`（陆地）和 `1`（水域）组成。一个岛屿是由一些相邻的 `0` 组成的最大 4 方向连通组。封闭岛屿是一个完全由 `1`（左、上、右、下）包围的岛屿。

请返回封闭岛屿的数目。

示例 1：

输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭的，因为它们完全被水域（1 组成的组）包围。

示例 2：

输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1

示例 3：

输入：grid = [[1,1,1,1,1,1,1],
[1,0,0,0,0,0,1],
[1,0,1,1,1,0,1],
[1,0,1,0,1,0,1],
[1,0,1,1,1,0,1],
[1,0,0,0,0,0,1],
[1,1,1,1,1,1,1]]
输出：2

约束条件：

`1 <= grid.length, grid[0].length <= 100`

`0 <= grid[i][j] <= 1`
"""

from typing import List, Optional


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> bool:
            # If out of bounds, this is not a closed island
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            # If water or already visited, return True (doesn't invalidate closed)
            if grid[r][c] == 1:
                return True

            # Mark as visited
            grid[r][c] = 1

            # DFS in 4 directions; result is True only if ALL directions are closed
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return up and down and left and right

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# DFS 深度优先搜索。封闭岛屿的关键特征是：它不触碰网格边界。
# 1. 遍历网格中的每个陆地单元格 (grid[i][j] == 0)，启动 DFS。
# 2. DFS 过程中：
#    - 如果越界（超出网格范围），说明该岛屿触碰到了边界，不是封闭的，返回 False。
#    - 如果遇到水域 (1) 或已访问过的陆地，返回 True（不影响封闭判断）。
#    - 将当前陆地标记为已访问（置为 1）。
#    - 向四个方向递归，用 AND 汇总结果：只有四个方向都不越界（都是封闭的），当前岛屿才是封闭的。
# 3. 如果 DFS 返回 True，说明找到了一个封闭岛屿，计数 +1。
# 4. 也可以采用另一种策略：先将与边界相连的陆地全部"淹没"（Flood Fill），
#    再统计剩余的岛屿数量——这些剩余的岛屿一定不接触边界，即为封闭岛屿。
#
# 时间复杂度: O(M * N)，每个单元格最多被访问一次
# 空间复杂度: O(M * N)，递归栈的最坏深度
#
# 关键点:
# - 封闭岛屿的定义：不允许触碰网格边界
# - 越界条件：r < 0 or r >= m or c < 0 or c >= n 即说明该岛屿接触了边界
# - 遇到已访问或水域时返回 True（因为只有越界才会使岛屿"不封闭"）
# - 用 AND 聚合四个方向的返回值：四个方向都必须不越界，岛屿才是封闭的
# - 替代方案：先 Flood Fill 边界陆地，再 DFS 统计内部岛屿
