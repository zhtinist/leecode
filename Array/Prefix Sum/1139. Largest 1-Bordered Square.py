"""
LeetCode #1139 - Largest 1-Bordered Square
中文题名：最大的以 1 为边界的正方形
https://leetcode.com/problems/largest-1-bordered-square/

Given a 2D `grid` of `0`s and `1`s, return the number of
elements in the largest square subgrid that has all
`1`s on its border, or `0` if such a subgrid doesn't
exist in the `grid`.

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9

Example 2:

Input: grid = [[1,1,0,0]]
Output: 1

Constraints:

`1 <= grid.length <= 100`

`1 <= grid[0].length <= 100`

`grid[i][j]` is `0` or `1`

【中文翻译】
给定一个由 0 和 1 组成的二维网格 grid，返回边界全部由 1 组成的最大正方形子网格中的元素数量。
如果不存在这样的子网格，返回 0。

示例 1：

输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9

示例 2：

输入：grid = [[1,1,0,0]]
输出：1

约束条件：

`1 <= grid.length <= 100`

`1 <= grid[0].length <= 100`

`grid[i][j]` 是 `0` 或 `1`
"""

from typing import List, Optional


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left = [[0] * n for _ in range(m)]
        top = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    left[i][j] = left[i][j - 1] + 1 if j > 0 else 1
                    top[i][j] = top[i - 1][j] + 1 if i > 0 else 1

        max_side = 0
        for i in range(m):
            for j in range(n):
                side = min(left[i][j], top[i][j])
                while side > max_side:
                    if top[i][j - side + 1] >= side and left[i - side + 1][j] >= side:
                        max_side = side
                        break
                    side -= 1

        return max_side * max_side










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用前缀和预处理 + 枚举正方形的右下角。
# 1. 预处理两个辅助矩阵：
#    - left[i][j]：从 (i, j) 开始向左连续 1 的个数。
#    - top[i][j]：从 (i, j) 开始向上连续 1 的个数。
# 2. 枚举每个位置 (i, j) 作为正方形的右下角。
# 3. 当前可能的最大边长 side = min(left[i][j], top[i][j])。
# 4. 从 side 向下递减检查：
#    - 检查上边界：top[i][j - side + 1] >= side（左边竖边）。
#    - 检查左边界：left[i - side + 1][j] >= side（上边横边）。
#    - 若满足，更新 max_side。
# 5. 优化：仅当 side > max_side 时才检查（剪枝）。
# 6. 返回 max_side * max_side。
#
# 时间复杂度: O(m * n * min(m, n)) - 最坏情况下每个位置检查 O(min(m,n)) 次
# 空间复杂度: O(m * n) - 辅助矩阵
#
# 关键点:
# - left/top 前缀和数组是处理"连续 1"问题的常用技巧
# - 从 large 到 small 检查边长并剪枝可以大幅减少不必要的检查
