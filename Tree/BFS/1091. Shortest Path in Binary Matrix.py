"""
LeetCode #1091 - Shortest Path in Binary Matrix
中文题名：二进制矩阵中的最短路径
https://leetcode.com/problems/shortest-path-in-binary-matrix/

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length `k`
if and only if it is composed of cells `C_1, C_2, ..., C_k` such that:

Adjacent cells `C_i` and `C_{i+1}` are connected 8-directionally
(ie., they are different and share an edge or corner)

`C_1` is at location `(0, 0)` (ie. has value
`grid[0][0]`)

`C_k` is at location `(N-1, N-1)` (ie. has value `grid[N-1][N-1]`)

If `C_i` is located at `(r, c)`, then `grid[r][c]`
is empty (ie. `grid[r][c] == 0`).

Return the length of the shortest such clear path from top-left to bottom-right.  If
such a path does not exist, return -1.

Example 1:

Input: [[0,1],[1,0]]

Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]

Output: 4

【中文翻译】
在一个 N x N 的方格网格中，每个单元格有两种状态：空（0）或者阻塞（1）。

一条从左上角到右下角、长度为 k 的畅通路径，由满足下述条件的单元格 C_1, C_2, ..., C_k 组成：

相邻单元格 C_i 和 C_{i+1} 在八个方向之一上连通（即它们不同且共享边或角）
C_1 位于 (0, 0)（即网格的左上角 grid[0][0]）
C_k 位于 (N-1, N-1)（即网格的右下角 grid[N-1][N-1]）
如果 C_i 位于 (r, c)，则 grid[r][c] 为空（即 grid[r][c] == 0）。

返回这条从左上角到右下角的最短畅通路径的长度。如果不存在这样的路径，返回 -1。

示例 1：

输入：[[0,1],[1,0]]
输出：2

示例 2：

输入：[[0,0,0],[1,1,0],[1,1,0]]
输出：4

"""

from typing import List, Optional


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque

        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        q = deque([(0, 0)])
        grid[0][0] = 1

        step = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return step

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        q.append((nr, nc))
                        grid[nr][nc] = 1
            step += 1

        return -1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 BFS（广度优先搜索）在 8 方向网格中找最短路径。
# BFS 保证首次到达目标时的步数即为最短路径长度。
# 1. 检查起点和终点是否为 0（可通行），否则直接返回 -1。
# 2. 使用队列进行 BFS，按层遍历（每一层对应一步）。
# 3. 访问过的单元格标记为 1（已访问），避免重复访问。
# 4. 八个方向：上下左右 + 四个对角线。
# 5. 当到达 (n-1, n-1) 时返回当前步数 step。
# 6. 队列为空仍未到达，返回 -1。
#
# 时间复杂度: O(n^2) - 每个单元格最多访问一次
# 空间复杂度: O(n^2) - 队列最坏情况
#
# 关键点:
# - BFS 保证最短路径（无权图）
# - 起点和终点必须是 0（可通行）
# - 8 方向移动（包括对角线）
# - 直接修改 grid 标记访问，节省 visited 集合空间
# - 按层遍历记录步数
