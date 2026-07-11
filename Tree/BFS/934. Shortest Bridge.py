"""
LeetCode #934 - Shortest Bridge
中文题名：最短的桥
https://leetcode.com/problems/shortest-bridge/

In a given 2D binary array `A`, there are two islands.  (An island is a
4-directionally connected group of `1`s not connected to any other 1s.)

Now, we may change `0`s to `1`s so as to connect the two islands
together to form 1 island.

Return the smallest number of `0`s that must be flipped.  (It is guaranteed
that the answer is at least 1.)

Example 1:

Input: [[0,1],[1,0]]
Output: 1

Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

【中文翻译】
给定一个二维二进制数组 A，其中包含两座岛。（岛是由 4 个方向相连的 1 组成
的最大组，且不与其他 1 相连。）

现在，我们可以将 0 变为 1，以便将两座岛连接在一起形成一座岛。

返回必须翻转的 0 的最小数目。（保证答案至少为 1。）

"""

from typing import List, Optional
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Step 1: DFS to find the first island and mark its cells as 2
        def dfs(i: int, j: int, queue: deque):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            queue.append((i, j))
            for di, dj in directions:
                dfs(i + di, j + dj, queue)

        queue = deque()
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, queue)
                    found = True
                    break

        # Step 2: BFS from the first island to find the second island
        distance = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            return distance
                        if grid[ni][nj] == 0:
                            grid[ni][nj] = 2
                            queue.append((ni, nj))
            distance += 1

        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. DFS 找到第一座岛：遍历网格，找到第一个 '1'，使用 DFS 将该岛的所有单元格
#    标记为 '2'，同时将这些坐标加入 BFS 队列中作为多源 BFS 的起点。
# 2. BFS 寻找最短桥：从第一座岛的边界开始进行 BFS。每轮 BFS 向外扩展一层（将
#    遇到的 '0' 变为 '2'），记录层数。当 BFS 首次遇到值为 '1'（第二座岛）的
#    单元格时，当前的层数（距离）即为需要翻转的最少 0 的数量。
# 3. 多源 BFS 保证找到的是最短路径。
#
# 时间复杂度: O(N^2) — 其中 N 是网格边长。DFS 和 BFS 各访问每个单元格最多一次。
# 空间复杂度: O(N^2) — BFS 队列在最坏情况下可能存储所有岛屿边界单元格。
#
# 关键点:
# - 使用 DFS 标记第一座岛并为 BFS 收集起始点
# - 多源 BFS 从第一座岛的整个边界同时向外扩展
# - 当 BFS 遇到第二座岛的任一单元格时立即返回当前距离
