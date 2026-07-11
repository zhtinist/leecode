"""
LeetCode #807 - Max Increase to Keep City Skyline
中文题名：保持城市天际线的最大增量
https://leetcode.com/problems/max-increase-to-keep-city-skyline/

In a 2 dimensional array `grid`, each value `grid[i][j]` represents the
height of a building located there. We are allowed to increase the height of any number of
buildings, by any amount (the amounts can be different for different buildings). Height 0
is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid,
i.e. top, bottom, left, and right, must be the same as the skyline of the
original grid. A city's skyline is the outer contour of the rectangles formed by all the
buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation:
The grid is:
[ [3, 0, 8, 4],
[2, 4, 5, 7],
[9, 2, 6, 3],
[0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
[7, 4, 7, 7],
[9, 4, 8, 7],
[3, 3, 3, 3] ]

Notes:

`1 < grid.length = grid[0].length <= 50`.

All heights `grid[i][j]` are in the range `[0, 100]`.

All buildings in `grid[i][j]` occupy the entire grid cell: that is, they are
a `1 x 1 x grid[i][j]` rectangular prism.

【中文翻译】
在一个二维数组 `grid` 中，每个值 `grid[i][j]` 代表位于该处建筑的高度。我们可以增加任意数量的建筑的高度，增加量可以不同。高度 0 也被视为建筑。

最终，从网格的四个方向（即上、下、左、右）观看的"天际线"必须与原始网格的天际线相同。城市的天际线是从远处观看时由所有建筑形成的矩形的外轮廓。参见以下示例。

建筑高度的最大总增加量是多少？

示例：
输入：grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
输出：35
解释：
网格为：
[ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

从上或下观看的天际线是：[9, 4, 8, 7]
从左或右观看的天际线是：[8, 7, 9, 3]

在不影响天际线的情况下增加建筑高度后的网格为：
gridNew =  [ [8, 4, 8, 7],
             [7, 4, 7, 7],
             [9, 4, 8, 7],
             [3, 3, 3, 3] ]

注意：
`1 < grid.length = grid[0].length <= 50`。
所有高度 `grid[i][j]` 在 `[0, 100]` 范围内。
所有建筑 `grid[i][j]` 占据整个网格单元：即它们是一个 `1 x 1 x grid[i][j]` 的矩形棱柱。
"""

from typing import List, Optional


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]

        total = 0
        for i in range(n):
            for j in range(n):
                limit = min(row_max[i], col_max[j])
                total += limit - grid[i][j]

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 天际线由每行和每列的最大高度决定。对于位置 (i, j)，
# 建筑最多可以增加到 min(row_max[i], col_max[j])，
# 因为超过这个高度会改变行的天际线或列的天际线。
#
# 1. 计算每行的最大值 row_max
# 2. 计算每列的最大值 col_max
# 3. 遍历每个位置，累加 min(row_max[i], col_max[j]) - grid[i][j]
#
# 时间复杂度: O(N^2) - 遍历整个 N x N 网格
# 空间复杂度: O(N) - 存储行和列的最大值
#
# 关键点:
# - 每个位置独立受行和列最大值的双重约束
# - 增加量 = min(行最大值, 列最大值) - 当前高度
# - 由于每个位置取行和列最大值的较小者，天际线保持不变
