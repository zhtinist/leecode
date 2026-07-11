"""
LeetCode #2482 - Difference Between Ones and Zeros in Row and Column
行和列中一和零的差值
https://leetcode.cn/problems/difference-between-ones-and-zeros-in-row-and-column/

给你一个下标从 0 开始的 `m x n` 二进制矩阵 `grid` 。
我们按照如下过程，定义一个下标从 0 开始的 `m x n` 差值矩阵 `diff` ：
令第 `i` 行一的数目为 `onesRow_i` 。
令第 `j` 列一的数目为 `onesCol_j`_ 。
令第 `i` 行零的数目为 `zerosRow_i` 。
令第 `j` 列零的数目为 `zerosCol_j` 。
`diff[i][j] = onesRow_i + onesCol_j - zerosRow_i - zerosCol_j`
请你返回差值矩阵 `diff` 。

示例 1：

输入：grid = [[0,1,1],[1,0,1],[0,0,1]] 输出：[[0,0,4],[0,0,4],[-2,-2,2]] 解释： - diff[0][0] = `onesRow_0 + onesCol_0 - zerosRow_0 - zerosCol_0` = 2 + 1 - 1 - 2 = 0  - diff[0][1] = `onesRow_0 + onesCol_1 - zerosRow_0 - zerosCol_1` = 2 + 1 - 1 - 2 = 0  - diff[0][2] = `onesRow_0 + onesCol_2 - zerosRow_0 - zerosCol_2` = 2 + 3 - 1 - 0 = 4  - diff[1][0] = `onesRow_1 + onesCol_0 - zerosRow_1 - zerosCol_0` = 2 + 1 - 1 - 2 = 0  - diff[1][1] = `onesRow_1 + onesCol_1 - zerosRow_1 - zerosCol_1` = 2 + 1 - 1 - 2 = 0  - diff[1][2] = `onesRow_1 + onesCol_2 - zerosRow_1 - zerosCol_2` = 2 + 3 - 1 - 0 = 4  - diff[2][0] = `onesRow_2 + onesCol_0 - zerosRow_2 - zerosCol_0` = 1 + 1 - 2 - 2 = -2 - diff[2][1] = `onesRow_2 + onesCol_1 - zerosRow_2 - zerosCol_1` = 1 + 1 - 2 - 2 = -2 - diff[2][2] = `onesRow_2 + onesCol_2 - zerosRow_2 - zerosCol_2` = 1 + 3 - 2 - 0 = 2
示例 2：

输入：grid = [[1,1,1],[1,1,1]] 输出：[[5,5,5],[5,5,5]] 解释： - diff[0][0] = onesRow_0 + onesCol_0 - zerosRow_0 - zerosCol_0 = 3 + 2 - 0 - 0 = 5 - diff[0][1] = onesRow_0 + onesCol_1 - zerosRow_0 - zerosCol_1 = 3 + 2 - 0 - 0 = 5 - diff[0][2] = onesRow_0 + onesCol_2 - zerosRow_0 - zerosCol_2 = 3 + 2 - 0 - 0 = 5 - diff[1][0] = onesRow_1 + onesCol_0 - zerosRow_1 - zerosCol_0 = 3 + 2 - 0 - 0 = 5 - diff[1][1] = onesRow_1 + onesCol_1 - zerosRow_1 - zerosCol_1 = 3 + 2 - 0 - 0 = 5 - diff[1][2] = onesRow_1 + onesCol_2 - zerosRow_1 - zerosCol_2 = 3 + 2 - 0 - 0 = 5

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 10^5`
`1 <= m * n <= 10^5`
`grid[i][j]` 要么是 `0` ，要么是 `1` 。
"""

from typing import List, Optional


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        ones_row = [0] * m
        ones_col = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones_row[i] += 1
                    ones_col[j] += 1

        # diff[i][j] = onesRow_i + onesCol_j - zerosRow_i - zerosCol_j
        # zerosRow_i = n - onesRow_i, zerosCol_j = m - onesCol_j
        # => diff[i][j] = 2*onesRow_i + 2*onesCol_j - n - m
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * ones_row[i] + 2 * ones_col[j] - n - m

        return diff

# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Simulation
#
# 解题思路:
# 先遍历矩阵统计每行和每列的 1 的个数。
# 利用公式简化：zerosRow_i = n - onesRow_i，zerosCol_j = m - onesCol_j。
# 代入 diff 公式得：diff[i][j] = onesRow_i + onesCol_j - (n - onesRow_i) - (m - onesCol_j)
# = 2 * onesRow_i + 2 * onesCol_j - n - m。
# 直接计算即可，无需单独统计 0 的个数。
#
# 时间复杂度: O(m * n)，遍历矩阵两次
# 空间复杂度: O(m + n)，存储每行每列的 1 的计数（不计算输出数组）
#
# 关键点:
# - 公式简化避免统计 0 的个数
# - diff[i][j] = 2*onesRow_i + 2*onesCol_j - n - m
