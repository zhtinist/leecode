"""
LeetCode #3286 - Find a Safe Walk Through a Grid
穿越网格图的安全路径
https://leetcode.cn/problems/find-a-safe-walk-through-a-grid/

给你一个 `m x n` 的二进制矩形 `grid` 和一个整数 `health` 表示你的健康值。
你开始于矩形的左上角 `(0, 0)` ，你的目标是矩形的右下角 `(m - 1, n - 1)` 。
你可以在矩形中往上下左右相邻格子移动，但前提是你的健康值始终是 正数 。
对于格子 `(i, j)` ，如果 `grid[i][j] = 1` ，那么这个格子视为 不安全 的，会使你的健康值减少 1 。
如果你可以到达最终的格子，请你返回 `true` ，否则返回 `false` 。
注意 ，当你在最终格子的时候，你的健康值也必须为 正数 。

示例 1：

输入：grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1
输出：true
解释：
沿着下图中灰色格子走，可以安全到达最终的格子。
示例 2：

输入：grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3
输出：false
解释：
健康值最少为 4 才能安全到达最后的格子。
示例 3：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5
输出：true
解释：
沿着下图中灰色格子走，可以安全到达最终的格子。

任何不经过格子 `(1, 1)` 的路径都是不安全的，因为你的健康值到达最终格子时，都会小于等于 0 。

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 50`
`2 <= m * n`
`1 <= health <= m + n`
`grid[i][j]` 要么是 0 ，要么是 1 。
"""

from typing import List, Optional


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        import heapq
        m, n = len(grid), len(grid[0])
        # dist[i][j] = 到达 (i,j) 的最小生命值消耗
        dist = [[float('inf')] * n for _ in range(m)]
        start_cost = grid[0][0]
        if start_cost >= health:
            return False
        dist[0][0] = start_cost
        pq = [(start_cost, 0, 0)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while pq:
            cost, r, c = heapq.heappop(pq)
            if cost > dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return cost < health
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + grid[nr][nc]
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))
        return False










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Breadth-First Search, Graph, Array, Matrix, Shortest Path, Heap (Priority Queue)
#
# 解题思路:
# 问题等价于从 (0,0) 到 (m-1,n-1) 找到一条路径，使得路径上经过的不安全格子
# （grid[i][j]==1）的数量 < health。
# 使用 Dijkstra 算法，将每个格子的不安全程度 (0 或 1) 作为边的权重，
# 求到达每个位置的最小累计代价。
# 如果到达终点的最小代价 < health，返回 True。
#
# 时间复杂度: O(m*n * log(m*n))
# 空间复杂度: O(m*n)
#
# 关键点:
# - 转化为最短路径问题，边权重为 0 或 1
# - 也可以用 0-1 BFS（双端队列）优化，因为边权只有 0 和 1
