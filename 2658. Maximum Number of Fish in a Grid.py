"""
LeetCode #2658 - Maximum Number of Fish in a Grid
网格图中鱼的最大数目
https://leetcode.cn/problems/maximum-number-of-fish-in-a-grid/

给你一个下标从 0 开始大小为 `m x n` 的二维整数数组 `grid` ，其中下标在 `(r, c)` 处的整数表示：
如果 `grid[r][c] = 0` ，那么它是一块 陆地 。
如果 `grid[r][c] > 0` ，那么它是一块 水域 ，且包含 `grid[r][c]` 条鱼。
一位渔夫可以从任意 水域 格子 `(r, c)` 出发，然后执行以下操作任意次：
捕捞格子 `(r, c)` 处所有的鱼，或者
移动到相邻的 水域 格子。
请你返回渔夫最优策略下， 最多 可以捕捞多少条鱼。如果没有水域格子，请你返回 `0` 。
格子 `(r, c)` 相邻 的格子为 `(r, c + 1)` ，`(r, c - 1)` ，`(r + 1, c)` 和 `(r - 1, c)` ，前提是相邻格子在网格图内。

示例 1：

输入：grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]] 输出：7 解释：渔夫可以从格子 `(1,3)` 出发，捕捞 3 条鱼，然后移动到格子 `(2,3)` ，捕捞 4 条鱼。
示例 2：

输入：grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]] 输出：1 解释：渔夫可以从格子 (0,0) 或者 (3,3) ，捕捞 1 条鱼。

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 10`
`0 <= grid[i][j] <= 10`
"""

from typing import List, Optional


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        max_fish = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            if visited[r][c] or grid[r][c] == 0:
                return 0
            visited[r][c] = True
            total = grid[r][c]
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                total += dfs(r + dr, c + dc)
            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Union Find, Array, Matrix
#
# 解题思路:
# 使用DFS遍历每个连通的水域区域。从每个未访问的水域格子出发，递归访问四个方向的相邻水域，
# 累加鱼的数量。返回所有连通分量中的最大鱼数。陆地(grid=0)自动停止DFS。
#
# 时间复杂度: O(m * n)
# 空间复杂度: O(m * n)
#
# 关键点:
# - 水域连通分量问题，等价于无向图的连通分量和的最大值
# - 使用visited数组避免重复访问
# - grid[i][j]>0表示水域，=0表示陆地
