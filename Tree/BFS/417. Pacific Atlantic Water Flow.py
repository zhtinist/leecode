"""
LeetCode #417 - Pacific Atlantic Water Flow
中文题名：太平洋大西洋水流问题
https://leetcode.com/problems/pacific-atlantic-water-flow/

Given an `m x n` matrix of non-negative integers representing the height of each
unit cell in a continent, the "Pacific ocean" touches the left and top edges of
the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one
with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic
ocean.

Note:

The order of returned grid coordinates does not matter.

Both m and n are less than 150.

Example:

Given the following 5x5 matrix:

Pacific ~   ~   ~   ~   ~
~  1   2   2   3  (5) *
~  3   2   3  (4) (4) *
~  2   4  (5)  3   1  *
~ (6) (7)  1   4   5  *
~ (5)  1   1   2   4  *
*   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

【中文翻译】
给定一个 m x n 的非负整数矩阵，表示大陆上每个单元格的高度。
"太平洋"接触矩阵的左边缘和上边缘，"大西洋"接触矩阵的右边缘和下边缘。

水只能从高向低或等高处向四个方向（上、下、左、右）流动。

找出所有水可以同时流向太平洋和大西洋的网格坐标。

返回的网格坐标顺序不重要。m 和 n 均小于 150。
"""

from typing import List, Optional
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        pq = deque()
        aq = deque()
        for i in range(m):
            pacific[i][0] = True
            pq.append((i, 0))
            atlantic[i][n - 1] = True
            aq.append((i, n - 1))
        for j in range(n):
            pacific[0][j] = True
            pq.append((0, j))
            atlantic[m - 1][j] = True
            aq.append((m - 1, j))

        bfs(pq, pacific)
        bfs(aq, atlantic)

        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 逆向思维：从两个海洋边界出发 BFS/DFS，标记所有可以流向该海洋的单元格。
# 太平洋从左上边界出发，大西洋从右下边界出发。
# 水只能从低向高逆向流动（即 heights[nr][nc] >= heights[r][c]）。
# 最后取两个 visited 矩阵的交集，即能同时流向两大洋的单元格。
#
# 时间复杂度: O(m * n) — 每个单元格最多访问两次（太平洋一次、大西洋一次）
# 空间复杂度: O(m * n) — 两个 visited 矩阵 + BFS 队列
#
# 关键点:
# - 逆向思维：从海洋边界反向搜索比从每个单元格正向搜索更高效
# - BFS/DFS 均可，BFS 用队列、DFS 用递归栈
# - 条件 heights[nr][nc] >= heights[r][c] 保证水能逆向"爬升"


