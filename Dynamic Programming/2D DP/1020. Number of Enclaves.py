"""
LeetCode #1020 - Number of Enclaves
中文题名：飞地的数量
https://leetcode.com/problems/number-of-enclaves/

Given a 2D array `A`, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or
off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off
the boundary of the grid in any number of moves.

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation:
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.

Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation:
All 1s are either on the boundary or can reach the boundary.

Note:

`1 <= A.length <= 500`

`1 <= A[i].length <= 500`

`0 <= A[i][j] <= 1`

All rows have the same size.

【中文翻译】
给定一个二维数组 `A`，每个格子是 0（代表海洋）或 1（代表陆地）。

一次移动包括在四个方向上从一个陆地格子走到另一个陆地格子，或走出网格的边界。

返回网格中无法以任何数量的移动走出网格边界的陆地格子的数量。

示例 1：

输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：
有三个 1 被 0 包围，还有一个 1 没有被包围因为它位于边界上。

示例 2：

输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：
所有 1 都在边界上或可以到达边界。

注意：

`1 <= A.length <= 500`

`1 <= A[i].length <= 500`

`0 <= A[i][j] <= 1`

所有行大小相同。

"""

from typing import List, Optional


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 0
        m, n = len(A), len(A[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or A[i][j] == 0:
                return
            A[i][j] = 0
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + di, j + dj)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        return sum(sum(row) for row in A)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题要求统计无法到达边界的陆地数量，等价于统计不连接到边界的陆地。
# 使用 DFS 从四条边界上的陆地格子出发，将所有能到达边界的陆地标记为 0（或访问过）。
# 具体步骤：
# 1. 遍历四条边界，对值为 1 的格子启动 DFS，将相连的陆地全部置为 0。
# 2. DFS 递归访问四个方向，遇到 0（海洋或已访问）或越界时返回。
# 3. 遍历结束后，网格中剩余的 1 就是无法到达边界的飞地，求和即可。
#
# 时间复杂度: O(m * n) - 每个格子最多被访问一次
# 空间复杂度: O(m * n) - 递归调用栈最坏情况下需要访问全部陆地格子
#
# 关键点:
# - 从边界陆地出发进行 DFS 标记，而非从每个陆地出发检查是否能到边界
# - 将访问过的格子直接置 0（沉岛法），避免使用额外的 visited 数组
# - 最后通过 sum(sum(row) for row in A) 统计剩余的陆地数量
