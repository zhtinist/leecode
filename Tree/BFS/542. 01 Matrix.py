"""
LeetCode #542 - 01 Matrix
中文题名：01 矩阵
https://leetcode.com/problems/01-matrix/

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
[0,1,0],
[0,0,0]]

Output:
[[0,0,0],
[0,1,0],
[0,0,0]]

Example 2:

Input:
[[0,0,0],
[0,1,0],
[1,1,1]]

Output:
[[0,0,0],
[0,1,0],
[1,2,1]]

Note:

The number of elements of the given matrix will not exceed 10,000.

There are at least one 0 in the given matrix.

The cells are adjacent in only four directions: up, down, left and right.

【中文翻译】
给定一个由 0 和 1 组成的矩阵，找出每个单元格到最近的 0 的距离。相邻单元格间的距离为 1。
矩阵中至少有一个 0，相邻方向仅包括上下左右四个方向。

示例 1：
    输入：
    [[0,0,0],
     [0,1,0],
     [0,0,0]]
    输出：
    [[0,0,0],
     [0,1,0],
     [0,0,0]]

示例 2：
    输入：
    [[0,0,0],
     [0,1,0],
     [1,1,1]]
    输出：
    [[0,0,0],
     [0,1,0],
     [1,2,1]]
"""

from collections import deque
from typing import List, Optional


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        distances = [[-1] * cols for _ in range(rows)]

        # Initialize: enqueue all 0 cells
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    distances[r][c] = 0
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Multi-source BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and distances[nr][nc] == -1:
                    distances[nr][nc] = distances[r][c] + 1
                    queue.append((nr, nc))

        return distances



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用多源 BFS。将所有 0 的单元格作为起点同时加入队列（距离为 0），
# 将 1 的位置标记为 -1 表示未访问。然后进行 BFS 逐层扩散：
# 每次从队列取出一个单元格，探索其四个方向的邻居，若邻居未访问过，
# 则将其距离设为当前距离 + 1，并加入队列继续扩散。
# BFS 结束后，每个单元格的距离即为到最近 0 的最短距离。
#
# 时间复杂度: O(M * N) — 每个单元格最多入队一次
# 空间复杂度: O(M * N) — 队列空间和距离矩阵
#
# 关键点:
# - 多源 BFS 一次遍历即可求出所有单元格的最短距离
# - 将所有 0 作为初始起点同时入队，相当于同时从所有源头扩散
# - distances 矩阵同时承担 visited 作用：初始 0 距离为 0，1 标记为 -1 表示未访问
# - 也可以使用动态规划（两遍扫描），但 BFS 更直观
