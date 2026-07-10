"""
LeetCode #286 - Walls and Gates
https://leetcode.com/problems/walls-and-gates/

You are given a *m x n* 2D grid initialized with these three possible values.

`-1` - A wall or an obstacle.

`0` - A gate.

`INF` - Infinity means an empty room. We use the value `2^31 -
1 = 2147483647` to represent `INF` as you may assume that the distance
to a gate is less than `2147483647`.

Fill each empty room with the distance to its *nearest* gate. If it is impossible to
reach a gate, it should be filled with `INF`.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
0  -1 INF INF

After running your function, the 2D grid should be:

3  -1   0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4
"""

from typing import List, Optional


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """Fill each empty room with distance to nearest gate.

        Multi-source BFS starting from all gates simultaneously.
        Empty rooms (INF) are filled with the BFS level (distance).
        """
        if not rooms or not rooms[0]:
            return

        from collections import deque
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        queue = deque()

        # Enqueue all gates as starting points
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                # Skip out-of-bounds, walls, gates, or already visited rooms
                if r < 0 or r >= m or c < 0 or c >= n or rooms[r][c] != INF:
                    continue
                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 多源 BFS。同时从所有门（值为 0）开始进行广度优先搜索。每访问一个空房间，
# 将其值更新为当前距离（上一层房间的值 + 1），然后将其加入 BFS 队列继续扩散。
# 由于 BFS 按层遍历，第一次到达某个空房间时的距离就是最短距离。
# 墙（-1）和已访问的房间不会被重复处理，因为它们不再是 INF。
#
# 时间复杂度: O(M * N) - 每个单元格最多被访问一次
# 空间复杂度: O(M * N) - BFS 队列最坏情况包含所有单元格
#
# 关键点:
# - 多源 BFS：将所有门同时加入初始队列
# - BFS 保证第一次访问的距离是最短的
# - 使用 INF 值来判断房间是否已被访问（如果不再是 INF 说明已处理）
# - 墙（-1）和门（0）不会被更新
