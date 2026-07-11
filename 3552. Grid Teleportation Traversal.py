"""
LeetCode #3552 - Grid Teleportation Traversal
网格传送门旅游
https://leetcode.cn/problems/grid-teleportation-traversal/

给你一个大小为 `m x n` 的二维字符网格 `matrix`，用字符串数组表示，其中 `matrix[i][j]` 表示第 `i` 行和第 `j` 列处的单元格。每个单元格可以是以下几种字符之一：
`'.'` 表示一个空单元格。
`'#'` 表示一个障碍物。
一个大写字母（`'A'` 到 `'Z'`）表示一个传送门。
你从左上角单元格 `(0, 0)` 出发，目标是到达右下角单元格 `(m - 1, n - 1)`。你可以从当前位置移动到相邻的单元格（上、下、左、右），移动后的单元格必须在网格边界内且不是障碍物。
如果你踏入一个包含传送门字母的单元格，并且你之前没有使用过该传送门字母，你可以立即传送到网格中另一个具有相同字母的单元格。这次传送不计入移动次数，但每个字母对应的传送门在旅程中 最多 只能使用一次。
返回到达右下角单元格所需的 最少 移动次数。如果无法到达目的地，则返回 `-1`。

示例 1：

输入： matrix = ["A..",".A.","..."]
输出： 2
解释：

在第一次移动之前，从 `(0, 0)` 传送到 `(1, 1)`。
第一次移动，从 `(1, 1)` 移动到 `(1, 2)`。
第二次移动，从 `(1, 2)` 移动到 `(2, 2)`。
示例 2：

输入： matrix = [".#...",".#.#.",".#.#.","...#."]
输出： 13
解释：

提示：
`1 <= m == matrix.length <= 10^3`
`1 <= n == matrix[i].length <= 10^3`
`matrix[i][j]` 是 `'#'`、`'.'` 或一个大写英文字母。
`matrix[0][0]` 不是障碍物。
"""

from typing import List, Optional


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        from collections import deque

        # Group portal positions by letter
        portals = {}
        for i in range(m):
            for j in range(n):
                ch = matrix[i][j]
                if 'A' <= ch <= 'Z':
                    if ch not in portals:
                        portals[ch] = []
                    portals[ch].append((i, j))

        # BFS with 0-1 weights (teleport = 0 cost)
        INF = 10 ** 9
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        used_portal = set()

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()
            d = dist[r][c]

            if r == m - 1 and c == n - 1:
                return d

            # Check if current cell is an unused portal
            ch = matrix[r][c]
            if 'A' <= ch <= 'Z' and ch not in used_portal:
                used_portal.add(ch)
                for nr, nc in portals[ch]:
                    if (nr, nc) != (r, c) and dist[nr][nc] > d:
                        dist[nr][nc] = d
                        q.appendleft((nr, nc))  # 0-cost move

            # Normal 4-directional moves
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#':
                    if dist[nr][nc] > d + 1:
                        dist[nr][nc] = d + 1
                        q.append((nr, nc))

        return -1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Breadth-First Search, Array, Hash Table, Matrix
#
# 解题思路:
# 使用 0-1 BFS 求最短路径。普通移动（上下左右）代价为 1，传送门移动代价为 0。
# 预处理：将所有传送门位置按字母分组存入哈希表。
# BFS 过程中，当首次踏上一个未使用过的传送门字母时，将该字母的所有其他传送门位置加入队列前端（0 代价），同时标记该字母已使用。
# 使用双端队列（deque）：普通移动逐格走，加到队尾；传送门移动 0 代价，加到队首。
# 到达右下角时返回当前距离；BFS 结束未到达则返回 -1。
#
# 时间复杂度: O(m * n)，每个单元格最多入队一次。传送门最多触发 26 次，每次 O(该字母出现次数)，总开销 O(m*n)。
# 空间复杂度: O(m * n)，距离数组和队列。
#
# 关键点:
# - 传送门 0 代价，用双端队列实现 0-1 BFS（appendleft 而非特殊处理）。
# - 每个字母的传送门只能使用一次，用集合记录已使用的字母。
# - 传送门不计入移动次数，到达传送门后立即可以 0 代价跳到同字母另一位置。
