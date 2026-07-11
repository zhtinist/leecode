"""
LeetCode #2428 - Maximum Sum of an Hourglass
沙漏的最大总和
https://leetcode.cn/problems/maximum-sum-of-an-hourglass/

给你一个大小为 `m x n` 的整数矩阵 `grid` 。
按以下形式将矩阵的一部分定义为一个 沙漏 ：
返回沙漏中元素的 最大 总和。
注意：沙漏无法旋转且必须整个包含在矩阵中。

示例 1：
输入：grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]] 输出：30 解释：上图中的单元格表示元素总和最大的沙漏：6 + 2 + 1 + 2 + 9 + 2 + 8 = 30 。
示例 2：
输入：grid = [[1,2,3],[4,5,6],[7,8,9]] 输出：35 解释：上图中的单元格表示元素总和最大的沙漏：1 + 2 + 3 + 5 + 7 + 8 + 9 = 35 。

提示：
`m == grid.length`
`n == grid[i].length`
`3 <= m, n <= 150`
`0 <= grid[i][j] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_sum = 0

        for i in range(m - 2):
            for j in range(n - 2):
                # Hourglass shape:
                #  A B C
                #    D
                #  E F G
                cur = (
                    grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                    + grid[i + 1][j + 1]
                    + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                )
                if cur > max_sum:
                    max_sum = cur

        return max_sum



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Prefix Sum
#
# 解题思路:
# 沙漏形状为一个 3x3 区域中除去 (r+1, c) 和 (r+1, c+2) 两个位置
# 后的 7 个元素。直接枚举所有可能的沙漏左上角位置：
# 行范围 [0, m-3]，列范围 [0, n-3]。
# 对每个左上角 (i, j)，计算 7 个元素的和并更新最大值。
#
# 时间复杂度: O(m * n) — 每个可能的左上角做 O(1) 的 7 元素求和
# 空间复杂度: O(1) — 只使用常数额外空间
#
# 关键点:
# - 沙漏形状固定，无需旋转
# - 矩阵较小（m,n <= 150），直接 O(m*n) 枚举即可通过
# - 7 个元素位置：(i,j), (i,j+1), (i,j+2), (i+1,j+1), (i+2,j), (i+2,j+1), (i+2,j+2)
