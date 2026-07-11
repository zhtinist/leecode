"""
LeetCode #1905 - Count Sub Islands
统计子岛屿
https://leetcode.cn/problems/count-sub-islands/

给你两个 `m x n` 的二进制矩阵 `grid1` 和 `grid2` ，它们只包含 `0` （表示水域）和 `1` （表示陆地）。一个 岛屿 是由 四个方向 （水平或者竖直）上相邻的 `1` 组成的区域。任何矩阵以外的区域都视为水域。
如果 `grid2` 的一个岛屿，被 `grid1` 的一个岛屿 完全 包含，也就是说 `grid2` 中该岛屿的每一个格子都被 `grid1` 中同一个岛屿完全包含，那么我们称 `grid2` 中的这个岛屿为 子岛屿 。
请你返回 `grid2` 中 子岛屿 的 数目 。

示例 1：
输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]] 输出：3 解释：如上图所示，左边为 grid1 ，右边为 grid2 。 grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
示例 2：
输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]] 输出：2  解释：如上图所示，左边为 grid1 ，右边为 grid2 。 grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。

提示：
`m == grid1.length == grid2.length`
`n == grid1[i].length == grid2[i].length`
`1 <= m, n <= 500`
`grid1[i][j]` 和 `grid2[i][j]` 都要么是 `0` 要么是 `1` 。
"""

from typing import List, Optional


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int) -> bool:
            # Returns True if the island in grid2 is a sub-island of grid1
            if r < 0 or r >= m or c < 0 or c >= n or grid2[r][c] == 0:
                return True

            grid2[r][c] = 0  # Mark as visited

            # If this cell is water in grid1, this island is not a sub-island
            is_sub = (grid1[r][c] == 1)

            for dr, dc in directions:
                # Use bitwise AND to accumulate - if any part fails, whole fails
                is_sub &= dfs(r + dr, c + dc)

            return is_sub

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Union Find, Array, Matrix
#
# 解题思路:
# DFS 遍历 grid2 中的每个岛屿，同时检查是否被 grid1 完全包含。
# 1. 遍历 grid2 的每个格子，如果为 1（未访问的陆地），启动 DFS。
# 2. DFS 过程中标记已访问（将 grid2[r][c] 设为 0）。
# 3. 对于岛屿中的每个格子，检查 grid1 中对应位置是否为陆地。
#    如果所有格子都在 grid1 中也是陆地，则是子岛屿。
# 4. 使用 AND 逻辑累加：只要有一个格子不满足，整个岛屿就不是子岛屿。
#
# 时间复杂度: O(m * n) — 每个格子访问一次
# 空间复杂度: O(m * n) — 递归栈深度最坏情况
#
# 关键点:
# - 直接在 grid2 上修改标记已访问，节省空间
# - 使用 AND 运算确保岛屿的每个格子都满足条件
# - 子岛屿的定义：grid2 岛屿的所有格子必须在 grid1 的同一个岛屿中
# - 即使不满足子岛屿条件也要完整遍历岛屿（标记所有格子）
