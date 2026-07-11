"""
LeetCode #2257 - Count Unguarded Cells in the Grid
统计网格图中没有被保卫的格子数
https://leetcode.cn/problems/count-unguarded-cells-in-the-grid/

给你两个整数 `m` 和 `n` 表示一个下标从 0 开始的 `m x n` 网格图。同时给你两个二维整数数组 `guards` 和 `walls` ，其中 `guards[i] = [row_i, col_i]` 且 `walls[j] = [row_j, col_j]` ，分别表示第 `i` 个警卫和第 `j` 座墙所在的位置。
一个警卫能看到 4 个坐标轴方向（即东、南、西、北）的 所有 格子，除非他们被一座墙或者另外一个警卫 挡住 了视线。如果一个格子能被 至少 一个警卫看到，那么我们说这个格子被 保卫 了。
请你返回空格子中，有多少个格子是 没被保卫 的。

示例 1：

输入：m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]] 输出：7 解释：上图中，被保卫和没有被保卫的格子分别用红色和绿色表示。 总共有 7 个没有被保卫的格子，所以我们返回 7 。
示例 2：

输入：m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]] 输出：4 解释：上图中，没有被保卫的格子用绿色表示。 总共有 4 个没有被保卫的格子，所以我们返回 4 。

提示：
`1 <= m, n <= 10^5`
`2 <= m * n <= 10^5`
`1 <= guards.length, walls.length <= 5 * 10^4`
`2 <= guards.length + walls.length <= m * n`
`guards[i].length == walls[j].length == 2`
`0 <= row_i, row_j < m`
`0 <= col_i, col_j < n`
`guards` 和 `walls` 中所有位置 互不相同 。
"""

from typing import List, Optional


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Grid cell states:
        # 0 = unoccupied / unguarded
        # 1 = guard
        # 2 = wall
        # 3 = guarded (seen by at least one guard)
        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        # Row scans: left-to-right and right-to-left
        for i in range(m):
            # Left to right
            seeing = False
            for j in range(n):
                if grid[i][j] == 1:
                    seeing = True
                elif grid[i][j] == 2:
                    seeing = False
                elif seeing:
                    grid[i][j] = 3

            # Right to left
            seeing = False
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    seeing = True
                elif grid[i][j] == 2:
                    seeing = False
                elif seeing:
                    grid[i][j] = 3

        # Column scans: top-to-bottom and bottom-to-top
        for j in range(n):
            # Top to bottom
            seeing = False
            for i in range(m):
                if grid[i][j] == 1:
                    seeing = True
                elif grid[i][j] == 2:
                    seeing = False
                elif seeing:
                    grid[i][j] = 3

            # Bottom to top
            seeing = False
            for i in range(m - 1, -1, -1):
                if grid[i][j] == 1:
                    seeing = True
                elif grid[i][j] == 2:
                    seeing = False
                elif seeing:
                    grid[i][j] = 3

        # Count cells that remain unoccupied (neither guard, wall, nor guarded)
        return sum(cell == 0 for row in grid for cell in row)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Simulation
#
# 解题思路:
# 使用线性扫描方法，避免从每个警卫出发的 O(k * (m+n)) 暴力模拟。
# 网格状态编码：0=空闲，1=警卫，2=墙，3=被保卫。
#
# 算法分两步：
# 1. 行扫描（左->右 和 右->左）：
#    维护 seeing 标志。遇到警卫设为 True，遇到墙设为 False。
#    当 seeing=True 且当前格为 0 时，标记为 3。
# 2. 列扫描（上->下 和 下->上）：同样逻辑。
#
# 最后统计 grid 中值为 0 的单元格数量。
# 这种扫描方法确保每个单元格最多被访问 4 次（每方向一次），总复杂度 O(m*n)。
#
# 时间复杂度: O(m*n) — 网格中每个单元格被扫描 4 次（上、下、左、右各一次）
# 空间复杂度: O(m*n) — 存储网格状态
#
# 关键点:
# - 线性扫描替代暴力 BFS，将复杂度从 O(k*(m+n)) 降至 O(m*n)
# - 四方向扫描：行（左右）+ 列（上下）
# - 墙和警卫都能阻挡视线，扫描遇到时正确处理 seeing 标志
# - 只标记 0 格为 3，不覆盖警卫和墙
