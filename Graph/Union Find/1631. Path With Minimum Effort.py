"""
LeetCode #1631 - Path With Minimum Effort
中文题名：最小体力消耗路径
https://leetcode.com/problems/path-with-minimum-effort/

You are a hiker preparing for an upcoming hike. You are given `heights`,
a 2D array of size `rows x columns`, where `heights[row][col]`
represents the height of cell `(row, col)`. You are situated in the top-left
cell, `(0, 0)`, and you hope to travel to the bottom-right cell, `(rows-1,
columns-1)` (i.e., 0-indexed). You can move
up, down, left, or
right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in
heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left
cell to the bottom-right cell.

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:

`rows == heights.length`

`columns == heights[i].length`

`1 <= rows, columns <= 100`

`1 <= heights[i][j] <= 106`

【中文翻译】
给定一个 heights 矩阵，大小为 rows x columns，其中 heights[row][col] 表示该位置的高度。
从左上角 (0,0) 出发前往右下角 (rows-1, columns-1)，每次可以向上下左右四个方向移动。
一条路径的体力消耗定义为路径上相邻格子高度差绝对值的最大值。求最小体力消耗。

示例 1：
输入: heights = [[1,2,2],[3,8,2],[5,3,5]]
输出: 2
解释: 路径 [1,3,5,3,5] 的连续格最大绝对差为 2。这是最优路径。
"""

from typing import List, Optional
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        pq = [(0, 0, 0)]
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        while pq:
            effort, r, c = heapq.heappop(pq)
            if r == rows - 1 and c == cols - 1:
                return effort
            if effort > efforts[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))

        return 0
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# Dijkstra 算法变体。用优先队列存储 (当前路径最大体力消耗, 行, 列)。
# 每次取出体力消耗最小的节点进行扩展。向四个方向移动，新的体力消耗 = max(当前最大消耗, 两个格子的高度差)。
# 当第一次到达右下角时，该消耗值就是答案（因为优先队列保证最小消耗先出队）。
# 也可用二分搜索 + BFS/DFS 或并查集解法。
#
# 时间复杂度: O(M * N * log(M*N)) — Dijkstra
# 空间复杂度: O(M * N) — efforts 数组和优先队列
#
# 关键点:
# - 这里 Dijkstra 的代价不是累加而是取 max，但优先队列仍然适用
# - 第一次到达终点时的消耗即为最小值
