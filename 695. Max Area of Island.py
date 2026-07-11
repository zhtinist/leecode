"""
LeetCode #695 - Max Area of Island
中文题名：岛屿的最大面积
https://leetcode.com/problems/max-area-of-island/

Given a non-empty 2D array `grid` of 0's and 1's, an island is a
group of `1`'s (representing land) connected 4-directionally (horizontal or
vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum
area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return `6`. Note the answer is not 11, because the island must
be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]

Given the above grid, return `0`.

Note: The length of each dimension in the given `grid` does not exceed 50.

【中文翻译】
给定一个非空的二维数组 `grid`，由 0 和 1 组成。一个岛屿由一组 1（表示陆地）通过四方向（水平或垂直）连接而成。你可以假设网格的所有四条边都被水包围。

找出给定二维数组中岛屿的最大面积。（如果没有岛屿，则最大面积为 0。）

示例 1：

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

给定上述 grid，返回 `6`。注意答案不是 11，因为岛屿必须是四方向连接的。

示例 2：

[[0,0,0,0,0,0,0,0]]

给定上述 grid，返回 `0`。

注意：给定 `grid` 的每个维度的长度不超过 50。
"""

from typing import List, Optional


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS 遍历每个岛屿并计算面积。
# 遍历网格中所有为 1 的格子，每次发现一个未访问的陆地格子就启动 DFS：
# - DFS 返回以该格子为起点的岛屿面积。
# - 将访问过的格子标记为 0（沉岛法），避免重复计算。
# - 向四个方向递归探索，累加面积。
# 更新全局最大面积。
#
# 时间复杂度: O(m*n) - 每个格子最多访问一次
# 空间复杂度: O(m*n) - DFS 递归栈深度（最坏整个网格都是陆地）
#
# 关键点:
# - 沉岛法：访问后直接修改 grid[r][c] = 0
# - 四方向 DFS 返回面积累加值
# - 与 #200 岛屿数量类似，只是要计算面积而非计数
