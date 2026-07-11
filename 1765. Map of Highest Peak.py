"""
LeetCode #1765 - Map of Highest Peak
中文题名：地图中的最高点
https://leetcode.com/problems/map-of-highest-peak/

You are given an integer matrix `isWater` of size `m x n` that represents a map of land and water cells.

If `isWater[i][j] == 0`, cell `(i, j)` is a land cell.

If `isWater[i][j] == 1`, cell `(i, j)` is a water cell.

You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.

If the cell is a water cell, its height must be `0`.

Any two adjacent cells must have an absolute height difference of at most `1`. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix `height` of size `m x n` where `height[i][j]` is cell `(i, j)`'s height. If there are multiple solutions, return any of them.

Example 1:

Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

Example 2:

Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

Constraints:

`m == isWater.length`

`n == isWater[i].length`

`1 <= m, n <= 1000`

`isWater[i][j]` is `0` or `1`.

There is at least one water cell.

【中文翻译】
给定一个 m x n 的矩阵 isWater，isWater[i][j] = 1 表示水域，0 表示陆地。
需要给每个单元格分配一个高度值，满足：
- 水域高度必须为 0
- 任意两个相邻单元格的高度差绝对值必须为 1
返回一个高度矩阵，使得最高高度最大化。

示例 1：
输入: isWater = [[0,1],[0,0]]
输出: [[1,0],[2,1]]
解释: 水域(0,1)高度=0。从水域BFS向外递增高度。
"""

from typing import List, Optional
from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[-1] * n for _ in range(m)]
        queue = deque()

        # 将所有水域入队，高度为0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    queue.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] == -1:
                    heights[nr][nc] = heights[r][c] + 1
                    queue.append((nr, nc))

        return heights
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 多源 BFS。将所有水域（高度为0）作为起始点入队。
# BFS 逐层向外扩展，每扩展一层高度加1。
# 这样能保证：
# 1. 水域高度均为 0
# 2. 相邻格高度差绝对值为 1（BFS 天然保证）
# 3. 最高高度最大化（BFS 给每个格分配了距最近水域的最短距离）
#
# 时间复杂度: O(M * N) — 每个单元格访问一次
# 空间复杂度: O(M * N) — 高度矩阵和队列
#
# 关键点:
# - 多源 BFS 从所有水域同时开始
# - 高度 = 到最近水域的曼哈顿距离
# - heights 初始化为 -1 表示未访问
