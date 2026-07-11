"""
LeetCode #1162 - As Far from Land as Possible
中文题名：地图分析
https://leetcode.com/problems/as-far-from-land-as-possible/

Given an N x N `grid` containing only values `0` and
`1`, where `0` represents water and `1`
represents land, find a water cell such that its distance to the nearest land cell is
maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance
between two cells `(x0, y0)` and `(x1, y1)` is `|x0 - x1| + |y0 -
y1|`.

If no land or water exists in the grid, return `-1`.

Example 1:

Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation:
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation:
The cell (2, 2) is as far as possible from all the land with distance 4.

Note:

`1 <= grid.length == grid[0].length <= 100`

`grid[i][j]` is `0` or `1`

【中文翻译】
给定一个 N x N 的网格 grid，只包含值 0 和 1，其中 0 代表水域，1 代表陆地。找到一个水域单元格，使其到最近陆地单元格的距离最大化，并返回该距离。

本题中使用的距离为曼哈顿距离：两个单元格 (x0, y0) 和 (x1, y1) 之间的距离为 |x0 - x1| + |y0 - y1|。

如果网格中不存在陆地或不存在水域，返回 -1。

示例 1：

输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释：单元格 (1, 1) 到所有陆地的距离最远，距离为 2。

示例 2：

输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释：单元格 (2, 2) 到所有陆地的距离最远，距离为 4。

注意：

`1 <= grid.length == grid[0].length <= 100`

`grid[i][j]` 是 0 或 1
"""

from typing import List, Optional
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        # Add all land cells as BFS sources
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        # If no land or all land
        if not queue or len(queue) == n * n:
            return -1

        max_dist = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Multi-source BFS
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = grid[x][y] + 1
                    max_dist = max(max_dist, grid[nx][ny] - 1)
                    queue.append((nx, ny))

        return max_dist










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 多源 BFS（广度优先搜索）：
# 1. 将所有陆地单元格（值为 1）作为 BFS 的起点同时加入队列。
# 2. 使用 BFS 逐层扩展，将相邻的水域单元格标记为距离值。
#    具体地，grid[nx][ny] = grid[x][y] + 1，即当前距离 + 1。
# 3. BFS 过程中跟踪遇到的最远距离 max_dist = grid[nx][ny] - 1
#    （因为陆地本身距离为 1，实际曼哈顿距离需要减 1）。
# 4. 边界情况：如果没有陆地或全是陆地，返回 -1。
#
# 多源 BFS 的核心思想：同时从所有陆地出发，逐层向外扩散，
# 最先到达的水域距离最近陆地最近，最后到达的水域距离最远。
# 这等价于计算每个水域到最近陆地的曼哈顿距离。
#
# 时间复杂度: O(n^2) - 每个单元格最多入队一次
# 空间复杂度: O(n^2) - 队列最坏情况下存储所有单元格
#
# 关键点:
# - 多源 BFS：所有陆地同时作为起点，一次性加入队列
# - 距离计算：利用 grid 原地存储距离值，grid = 0 表示未访问的水域
# - 曼哈顿距离 = BFS 层数
# - 边界：无陆地或全是陆地时返回 -1
