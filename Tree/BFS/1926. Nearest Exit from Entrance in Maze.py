"""
LeetCode #1926 - Nearest Exit from Entrance in Maze
迷宫中离入口最近的出口
https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/

给你一个 `m x n` 的迷宫矩阵 `maze` （下标从 0 开始），矩阵中有空格子（用 `'.'` 表示）和墙（用 `'+'` 表示）。同时给你迷宫的入口 `entrance` ，用 `entrance = [entrance_row, entrance_col]` 表示你一开始所在格子的行和列。
每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 `entrance` 最近 的出口。出口 的含义是 `maze` 边界 上的 空格子。`entrance` 格子 不算 出口。
请你返回从 `entrance` 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 `-1` 。

示例 1：
输入：maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2] 输出：1 解释：总共有 3 个出口，分别位于 (1,0)，(0,2) 和 (2,3) 。 一开始，你在入口格子 (1,2) 处。 - 你可以往左移动 2 步到达 (1,0) 。 - 你可以往上移动 1 步到达 (0,2) 。 从入口处没法到达 (2,3) 。 所以，最近的出口是 (0,2) ，距离为 1 步。
示例 2：
输入：maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0] 输出：2 解释：迷宫中只有 1 个出口，在 (1,2) 处。 (1,0) 不算出口，因为它是入口格子。 初始时，你在入口与格子 (1,0) 处。 - 你可以往右移动 2 步到达 (1,2) 处。 所以，最近的出口为 (1,2) ，距离为 2 步。
示例 3：
输入：maze = [[".","+"]], entrance = [0,0] 输出：-1 解释：这个迷宫中没有出口。

提示：
`maze.length == m`
`maze[i].length == n`
`1 <= m, n <= 100`
`maze[i][j]` 要么是 `'.'` ，要么是 `'+'` 。
`entrance.length == 2`
`0 <= entrance_row < m`
`0 <= entrance_col < n`
`entrance` 一定是空格子。
"""

from typing import List, Optional


from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        er, ec = entrance

        queue = deque([(er, ec, 0)])  # (row, col, steps)
        visited = set()
        visited.add((er, ec))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c, steps = queue.popleft()

            # Check if this is an exit (boundary cell that's not the entrance)
            if (r != er or c != ec) and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in visited and
                    maze[nr][nc] == '.'):
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Breadth-First Search, Array, Matrix
#
# 解题思路:
# BFS 寻找最短路径。
# 1. 从入口开始进行广度优先搜索。
# 2. 记录每个位置的步数。
# 3. 当遇到边界格子且不是入口时，返回当前步数。
# 4. BFS 保证第一次遇到的出口就是最近的。
# 5. 如果 BFS 结束未找到出口，返回 -1。
#
# 时间复杂度: O(m * n) — 最坏情况遍历所有格子
# 空间复杂度: O(m * n) — visited 集合和队列
#
# 关键点:
# - 入口不算出口，即使它在边界上
# - BFS 保证最短路径
# - 需要 visited 集合避免重复访问
# - 迷宫中的 '+' 是墙，不能通过
