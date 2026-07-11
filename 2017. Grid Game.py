"""
LeetCode #2017 - Grid Game
网格游戏
https://leetcode.cn/problems/grid-game/

给你一个下标从 0 开始的二维数组 `grid` ，数组大小为 `2 x n` ，其中 `grid[r][c]` 表示矩阵中 `(r, c)` 位置上的点数。现在有两个机器人正在矩阵上参与一场游戏。
两个机器人初始位置都是 `(0, 0)` ，目标位置是 `(1, n-1)` 。每个机器人只会 向右 (`(r, c)` 到 `(r, c + 1)`) 或 向下 (`(r, c)` 到 `(r + 1, c)`) 。
游戏开始，第一个 机器人从 `(0, 0)` 移动到 `(1, n-1)` ，并收集路径上单元格的全部点数。对于路径上所有单元格 `(r, c)` ，途经后 `grid[r][c]` 会重置为 `0` 。然后，第二个 机器人从 `(0, 0)` 移动到 `(1, n-1)` ，同样收集路径上单元的全部点数。注意，它们的路径可能会存在相交的部分。
第一个 机器人想要打击竞争对手，使 第二个 机器人收集到的点数 最小化 。与此相对，第二个 机器人想要 最大化 自己收集到的点数。两个机器人都发挥出自己的 最佳水平 的前提下，返回 第二个 机器人收集到的 点数 。

示例 1：

输入：grid = [[2,5,4],[1,5,1]] 输出：4 解释：第一个机器人的最佳路径如红色所示，第二个机器人的最佳路径如蓝色所示。 第一个机器人访问过的单元格将会重置为 0 。 第二个机器人将会收集到 0 + 0 + 4 + 0 = 4 个点。
示例 2：
输入：grid = [[3,3,1],[8,5,2]] 输出：4 解释：第一个机器人的最佳路径如红色所示，第二个机器人的最佳路径如蓝色所示。  第一个机器人访问过的单元格将会重置为 0 。 第二个机器人将会收集到 0 + 3 + 1 + 0 = 4 个点。
示例 3：
输入：grid = [[1,3,1,15],[1,3,3,1]] 输出：7 解释：第一个机器人的最佳路径如红色所示，第二个机器人的最佳路径如蓝色所示。 第一个机器人访问过的单元格将会重置为 0 。 第二个机器人将会收集到 0 + 1 + 3 + 3 + 0 = 7 个点。

提示：
`grid.length == 2`
`n == grid[r].length`
`1 <= n <= 5 * 10^4`
`1 <= grid[r][c] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        # Prefix sums for top and bottom rows
        top_prefix = [0] * (n + 1)
        bottom_prefix = [0] * (n + 1)
        for i in range(n):
            top_prefix[i + 1] = top_prefix[i] + grid[0][i]
            bottom_prefix[i + 1] = bottom_prefix[i] + grid[1][i]

        # First robot wants to minimize second robot's maximum score
        # Try each column as the turning point (where robot 1 goes down)
        result = float('inf')
        for i in range(n):
            # Robot 1 goes down at column i
            # Robot 2 can either take the remaining top part (i+1 to n-1) or remaining bottom part (0 to i-1)
            top_remaining = top_prefix[n] - top_prefix[i + 1]
            bottom_remaining = bottom_prefix[i]
            second_best = max(top_remaining, bottom_remaining)
            result = min(result, second_best)
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Prefix Sum
#
# 解题思路:
# 第一个机器人的目标是让第二个机器人得分最小化。第一个机器人一定会从某列向下走，将格子分成
# 右上部分和左下部分。第二个机器人只能选择其中一部分收集。第一个机器人会选择让这两部分
# 的最大值最小的列作为转折点。遍历所有列，计算右上剩余和左下剩余的最大值，取最小值。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 第一个机器人只能在某列从第0行转向第1行
# - 第二个机器人只能收集右上或左下一部分
# - 使用前缀和快速计算区间和
