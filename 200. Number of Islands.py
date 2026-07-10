"""
LeetCode #200 - Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of `'1'`s (land) and `'0'`s
(water), count the number of islands. An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically. You may assume all four edges of the
grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

from typing import List, Optional


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"  # Mark as visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)  # Sink the entire island

        return count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS 淹没岛屿。遍历整个网格，当遇到 "1"（陆地）时：
# 1. 岛屿数量 count + 1
# 2. 从该位置开始 DFS，将所有相连的 "1" 改为 "0"（淹没整个岛屿）
# 3. 继续遍历，遇到下一个 "1" 说明发现了新岛屿
#
# DFS 递归探索四个方向（上下左右），将访问过的陆地标记为 "0" 避免重复访问。
# 这样每个岛屿被发现一次后就被完全淹没，不会重复计数。
#
# 时间复杂度: O(M * N) — 每个单元格最多访问两次（一次检查，一次淹没）
# 空间复杂度: O(M * N) — 最坏情况递归栈深度（整个网格都是陆地）
#
# 关键点:
# - DFS/BFS 淹没岛屿是经典做法
# - 将访问过的陆地改为 "0" 相当于原地标记，节省 visited 矩阵
# - 也可以用并查集 (Union-Find) 解决
