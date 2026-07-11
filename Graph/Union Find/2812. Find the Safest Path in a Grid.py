"""
LeetCode #2812 - Find the Safest Path in a Grid
找出最安全路径
https://leetcode.cn/problems/find-the-safest-path-in-a-grid/

给你一个下标从 0 开始、大小为 `n x n` 的二维矩阵 `grid` ，其中 `(r, c)` 表示：
如果 `grid[r][c] = 1` ，则表示一个存在小偷的单元格
如果 `grid[r][c] = 0` ，则表示一个空单元格
你最开始位于单元格 `(0, 0)` 。在一步移动中，你可以移动到矩阵中的任一相邻单元格，包括存在小偷的单元格。
矩阵中路径的 安全系数 定义为：从路径中任一单元格到矩阵中任一小偷所在单元格的 最小 曼哈顿距离。
返回所有通向单元格 `(n - 1, n - 1)` 的路径中的 最大安全系数 。
单元格 `(r, c)` 的某个 相邻 单元格，是指在矩阵中存在的 `(r, c + 1)`、`(r, c - 1)`、`(r + 1, c)` 和 `(r - 1, c)` 之一。
两个单元格 `(a, b)` 和 `(x, y)` 之间的 曼哈顿距离 等于 `| a - x | + | b - y |` ，其中 `|val|` 表示 `val` 的绝对值。

示例 1：
输入：grid = [[1,0,0],[0,0,0],[0,0,1]] 输出：0 解释：从 (0, 0) 到 (n - 1, n - 1) 的每条路径都经过存在小偷的单元格 (0, 0) 和 (n - 1, n - 1) 。
示例 2：
输入：grid = [[0,0,1],[0,0,0],[0,0,0]] 输出：2 解释： 上图所示路径的安全系数为 2： - 该路径上距离小偷所在单元格（0，2）最近的单元格是（0，0）。它们之间的曼哈顿距离为 | 0 - 0 | + | 0 - 2 | = 2 。 可以证明，不存在安全系数更高的其他路径。
示例 3：
输入：grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]] 输出：2 解释： 上图所示路径的安全系数为 2： - 该路径上距离小偷所在单元格（0，3）最近的单元格是（1，2）。它们之间的曼哈顿距离为 | 0 - 1 | + | 3 - 2 | = 2 。 - 该路径上距离小偷所在单元格（3，0）最近的单元格是（3，2）。它们之间的曼哈顿距离为 | 3 - 3 | + | 0 - 2 | = 2 。 可以证明，不存在安全系数更高的其他路径。

提示：
`1 <= grid.length == n <= 400`
`grid[i].length == n`
`grid[i][j]` 为 `0` 或 `1`
`grid` 至少存在一个小偷
"""

from typing import List, Optional


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        from collections import deque
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        def can_reach(k: int) -> bool:
            if dist[0][0] < k:
                return False
            visited = [[False] * n for _ in range(n)]
            q2 = deque()
            q2.append((0, 0))
            visited[0][0] = True
            while q2:
                x, y = q2.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and dist[nx][ny] >= k:
                        visited[nx][ny] = True
                        q2.append((nx, ny))
            return False

        lo, hi = 0, n * 2
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_reach(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Breadth-First Search, Union Find, Array, Binary Search, Matrix, Heap (Priority Queue)
#
# 解题思路:
# 多源 BFS 计算每个格子到最近小偷的曼哈顿距离（安全值）。
# 然后二分答案 + BFS/DFS 判断是否存在一条从 (0,0) 到 (n-1,n-1) 的路径，使得路径上所有格子的安全值都 >= k。
# 二分查找最大可行的 k 即为答案。
#
# 时间复杂度: O(n^2 * log n) 其中 n <= 400
# 空间复杂度: O(n^2)
#
# 关键点:
# - 多源 BFS 从所有小偷同时出发，计算每个格子的安全距离
# - 二分搜索最大安全系数 k
# - 验证函数用 BFS 检查是否存在一条所有格子安全值 >= k 的路径
