"""
LeetCode #1594 - Maximum Non Negative Product in a Matrix
中文题名：矩阵的最大非负积
https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/


You are given a `rows x cols` matrix `grid`. Initially,
you are located at the top-left corner `(0, 0)`, and in each
step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner `(0, 0)` and
ending in the bottom-right corner `(rows - 1, cols - 1)`, find the
path with the maximum non-negative product. The product of a
path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative
product modulo `109 + 7`. If
the maximum product is negative return `-1`.

Notice that the modulo is performed after getting the maximum
product.

Example 1:

Input: grid = [[-1,-2,-3],
[-2,-3,-3],
[-3,-3,-2]]
Output: -1
Explanation: It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.

Example 2:

Input: grid = [[1,-2,1],
[1,-2,1],
[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).

Example 3:

Input: grid = [[1, 3],
[0,-4]]
Output: 0
Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).

Example 4:

Input: grid = [[ 1, 4,4,0],
[-2, 0,0,1],
[ 1,-1,1,1]]
Output: 2
Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).

Constraints:

`1 <= rows, cols <= 15`

`-4 <= grid[i][j] <= 4`

【中文翻译】
给定 m x n 的网格 grid。从左上角 (0,0) 出发到右下角 (m-1,n-1)，
只能向右或向下移动。路径的乘积为经过的所有格子的值的乘积。
返回最大非负乘积对 10^9+7 取模的结果。如果最大乘积为负数，返回 -1。

示例 1：输入：grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
输出：-1

示例 2：输入：grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
输出：8
"""

from typing import List, Optional


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        for j in range(1, n):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j - 1] * grid[0][j]
        for i in range(1, m):
            dp_max[i][0] = dp_min[i][0] = dp_max[i - 1][0] * grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                candidates = [
                    dp_max[i - 1][j] * grid[i][j],
                    dp_min[i - 1][j] * grid[i][j],
                    dp_max[i][j - 1] * grid[i][j],
                    dp_min[i][j - 1] * grid[i][j],
                ]
                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)
        if dp_max[m - 1][n - 1] < 0:
            return -1
        return dp_max[m - 1][n - 1] % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。由于数字有正有负，乘积的最大值可能来自最大的正数相乘或最小的负数相乘（负负得正）。
# 需要同时维护到达每个位置的最大乘积和最小乘积。
# dp_max[i][j] = max(来自上方的 max/min * grid[i][j], 来自左方的 max/min * grid[i][j])。
# 最后检查 dp_max[m-1][n-1] 是否为非负数。
#
# 时间复杂度: O(M * N)
# 空间复杂度: O(M * N)
#
# 关键点:
# - 同时维护最大和最小乘积（负负得正）
# - 每个位置考虑从上方和左方来的 4 种组合
# - 取模在最后进行












