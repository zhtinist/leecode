"""
LeetCode #1034 - Coloring A Border
中文题名：边框着色
https://leetcode.com/problems/coloring-a-border/

Given a 2-dimensional `grid` of integers, each value in the grid represents
the color of the grid square at that location.

Two squares belong to the same connected component if and only if they have the same
color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected
component that are either 4-directionally adjacent to a square not in the
component, or on the boundary of the grid (the first or last row or column).

Given a square at location `(r0, c0)` in the grid and a
`color`, color the border of the connected component of that square with the
given `color`, and return the final `grid`.

Example 1:

Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]

Example 2:

Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]

Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]

【中文翻译】
给定一个二维整数网格 grid，网格中的每个值表示该位置网格方格的颜色。

两个方格属于同一个连通分量当且仅当它们颜色相同并且在四个方向中的任一方向上相邻。

连通分量的边界是指该连通分量中的所有方格，这些方格要么在四个方向上与不属于该分量的方格相邻，要么位于网格的边界（第一行或最后一行或第一列或最后一列）。

给定网格中位于 (r0, c0) 的一个方格和一个颜色 color，使用给定颜色 color 为该方格的连通分量的边界着色，并返回最终的网格。

示例 1：

输入：grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
输出：[[3, 3], [3, 2]]

示例 2：

输入：grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
输出：[[1, 3, 3], [2, 3, 3]]

示例 3：

输入：grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
输出：[[2, 2, 2], [2, 1, 2], [2, 2, 2]]
"""

from typing import List, Optional


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = set()
        border = set()
        original_color = grid[row][col]

        def dfs(r: int, c: int):
            visited.add((r, c))
            is_border = False

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    is_border = True
                elif grid[nr][nc] != original_color:
                    is_border = True
                elif (nr, nc) not in visited:
                    dfs(nr, nc)

            if is_border:
                border.add((r, c))

        dfs(row, col)

        for r, c in border:
            grid[r][c] = color

        return grid










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用深度优先搜索(DFS)遍历从 (r0, c0) 开始的连通分量。
# 对于分量中的每个单元格，检查其四个方向：
# - 如果某个方向超出网格边界，则该单元格是边界
# - 如果某个方向的相邻单元格颜色不同，则该单元格是边界
# - 如果相邻单元格颜色相同且未访问，继续DFS
# 收集所有边界单元格后，将它们替换为给定颜色。
#
# 时间复杂度: O(M * N) - 最坏情况下遍历整个网格
# 空间复杂度: O(M * N) - visited和border集合
#
# 关键点:
# - 先找出整个连通分量，再判断哪些是边界
# - 边界条件：网格边缘 OR 相邻颜色不同
# - 注意不能边遍历边修改，否则会影响后续DFS的颜色判断
