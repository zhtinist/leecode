"""
LeetCode #1706 - Where Will the Ball Fall
中文题名：球会落何处
https://leetcode.com/problems/where-will-the-ball-fall/

You have a 2-D `grid` of size `m x n` representing a box, and
you have `n` balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can
redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the
bottom-right corner and is represented in the grid as `1`.

A board that redirects the ball to the left spans the top-right corner to the
bottom-left corner and is represented in the grid as `-1`.

We drop one ball at the top of each column of the box. Each ball can get stuck in the
box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern
between two boards or if a board redirects the ball into either wall of the box.

Return an array `answer` of size `n`
where `answer[i]` is the column that the ball falls out of at
the bottom after dropping the ball from the `ith`
column at the top, or `-1` if the ball gets stuck in the
box.

Example 1:

Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

Example 2:

Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.

Constraints:

`m == grid.length`

`n == grid[i].length`

`1 <= m, n <= 100`

`grid[i][j]` is `1` or `-1`.

【中文翻译】
有一个大小为 `m x n` 的二维网格 `grid` 表示一个盒子，还有 `n` 个小球。
盒子的顶部和底部都是敞开的。

网格中的每个单元格都有一个跨单元格两角的斜板，可以将球导向右侧或左侧。

导向右侧的板跨越左上角到右下角，在网格中表示为 `1`。
导向左侧的板跨越右上角到左下角，在网格中表示为 `-1`。

在盒子的每一列顶部分别放入一个小球。每个球可能卡在盒子里，也可能从底部掉出。
如果球碰到两块板形成的"V"形图案，或者被板导向碰到盒子的任意一侧墙壁，球就会被卡住。

返回一个大小为 `n` 的数组 `answer`，其中 `answer[i]` 表示从第 `i` 列顶部放入的球从底部掉出的列号，
如果球被卡住则返回 `-1`。

示例 1：

输入: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
输出: [1,-1,-1,-1,-1]
解释: 如图所示
b0 从第 0 列放入，最终从第 1 列掉出
b1 从第 1 列放入，在第 1 行第 2 列和第 3 列之间卡住
b2 从第 2 列放入，在第 0 行第 2 列和第 3 列之间卡住
b3 从第 3 列放入，在第 0 行第 2 列和第 3 列之间卡住
b4 从第 4 列放入，在第 1 行第 2 列和第 3 列之间卡住

示例 2：

输入: grid = [[-1]]
输出: [-1]
解释: 球碰到左侧墙壁被卡住

约束条件：

`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 100`
`grid[i][j]` 为 `1` 或 `-1`
"""

from typing import List, Optional


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        模拟每个球的路径：
        对于每个起始列 c：
        - 从左到右逐行下降
        - 如果 grid[r][c] == 1，球向右滚：
          如果 c+1 < n 且 grid[r][c+1] == 1，则 c += 1，否则卡住
        - 如果 grid[r][c] == -1，球向左滚：
          如果 c-1 >= 0 且 grid[r][c-1] == -1，则 c -= 1，否则卡住
        - 如果成功穿过所有行，记录最终列号 c
        """
        m, n = len(grid), len(grid[0])
        result = []

        for start_col in range(n):
            col = start_col
            stuck = False
            for row in range(m):
                direction = grid[row][col]
                # 向右滚
                if direction == 1:
                    if col + 1 < n and grid[row][col + 1] == 1:
                        col += 1
                    else:
                        stuck = True
                        break
                # 向左滚
                else:  # direction == -1
                    if col - 1 >= 0 and grid[row][col - 1] == -1:
                        col -= 1
                    else:
                        stuck = True
                        break
            result.append(col if not stuck else -1)

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 模拟题。对于每个起始列（0 到 n-1），逐行模拟球的下降过程：
#
# 当前在 grid[row][col]：
# - grid[row][col] == 1（向右的斜板）：球会滚到右边的单元格 grid[row][col+1]
#   但要成功，必须满足：
#   1) col+1 在边界内
#   2) grid[row][col+1] 也必须是 1（否则形成 V 形，球卡住）
# - grid[row][col] == -1（向左的斜板）：球会滚到左边的单元格 grid[row][col-1]
#   但要成功，必须满足：
#   1) col-1 在边界内
#   2) grid[row][col-1] 也必须是 -1（否则形成 V 形，球卡住）
#
# 如果球成功穿过了所有行，记录最终列号；否则记录 -1。
#
# 时间复杂度: O(m * n)，每个球最多经过 m 行
# 空间复杂度: O(1) 额外空间（不算结果数组）
#
# 关键点:
# - V 形卡住条件：相邻两列方向相反（grid[r][c]!=grid[r][c+1] 当往右滚时）
# - 墙壁卡住条件：超出边界
# - 每个球独立模拟，m 和 n 都很小（<= 100），直接暴力即可
