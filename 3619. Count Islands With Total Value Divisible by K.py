"""
LeetCode #3619 - Count Islands With Total Value Divisible by K
总价值可以被 K 整除的岛屿数目
https://leetcode.cn/problems/count-islands-with-total-value-divisible-by-k/

给你一个 `m x n` 的矩阵 `grid` 和一个正整数 `k`。一个 岛屿 是由 正 整数（表示陆地）组成的，并且陆地间 四周 连通（水平或垂直）。
一个岛屿的总价值是该岛屿中所有单元格的值之和。
返回总价值可以被 `k` 整除 的岛屿数量。

示例 1:

输入: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
输出: 2
解释:
网格中包含四个岛屿。蓝色高亮显示的岛屿的总价值可以被 5 整除，而红色高亮显示的岛屿则不能。
示例 2:

输入: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
输出: 6
解释:
网格中包含六个岛屿，每个岛屿的总价值都可以被 3 整除。

提示:
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 1000`
`1 <= m * n <= 10^5`
`0 <= grid[i][j] <= 10^6`
`1 <= k < = 10^6`
"""

from typing import List, Optional


class Solution:
    def countIslandsDivisibleByK(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def get_island_sum(start_i: int, start_j: int) -> int:
            """Iterative DFS to find total value of one island."""
            stack = [(start_i, start_j)]
            visited[start_i][start_j] = True
            total = 0

            while stack:
                i, j = stack.pop()
                total += grid[i][j]
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < m and 0 <= nj < n
                            and not visited[ni][nj]
                            and grid[ni][nj] > 0):
                        visited[ni][nj] = True
                        stack.append((ni, nj))

            return total

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    island_sum = get_island_sum(i, j)
                    if island_sum % k == 0:
                        count += 1

        return count










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Union Find, Array, Matrix
#
# 解题思路:
# 标准的网格岛屿遍历问题，使用迭代 DFS（栈）或 BFS（队列）均可。
# 1. 遍历 grid 的每个单元格
# 2. 遇到正整数的未访问单元格时，启动岛屿遍历
#    - 用栈进行深度优先搜索，标记已访问
#    - 累加岛屿内所有单元格的值
# 3. 遍历完一个岛屿后，检查岛屿总价值是否能被 k 整除
#    - 若能整除，计数器 +1
# 4. 遍历完整个 grid 后返回计数器
#
# 使用迭代 DFS 而非递归，避免在极端情况下（岛屿大小为 10^5）的递归栈溢出。
#
# 时间复杂度: O(m * n) — 每个单元格最多被访问一次
# 空间复杂度: O(m * n) — visited 数组，栈最坏情况 O(m * n)
#
# 关键点:
# - 岛屿定义为正整数的四连通区域（上下左右），0 表示水域
# - 使用 visited 数组避免重复访问
# - 迭代遍历而非递归，防止栈溢出
# - 边遍历边求和，最后检查整除性
