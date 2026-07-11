"""
LeetCode #1727 - Largest Submatrix With Rearrangements
中文题名：重新排列后的最大子矩阵
https://leetcode.com/problems/largest-submatrix-with-rearrangements/

You are given a binary matrix `matrix` of size `m x n`, and
you are allowed to rearrange the columns of the `matrix` in
any order.

Return the area of the largest submatrix within `matrix`
where every element of the submatrix is `1`
after reordering the columns optimally.

Example 1:

Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.

Example 2:

Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.

Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.

Example 4:

Input: matrix = [[0,0],[0,0]]
Output: 0
Explanation: As there are no 1s, no submatrix of 1s can be formed and the area is 0.

Constraints:

`m == matrix.length`

`n == matrix[i].length`

`1 <= m * n <= 105`

`matrix[i][j]` is `0` or `1`.

【中文翻译】
给定一个 m x n 的二进制矩阵 matrix，可以按任意顺序重新排列每一行的列（但不能交换不同行的元素）。
求全为 1 的最大矩形子矩阵面积（即只包含1的子矩阵中最大的元素个数）。

示例 1：
输入: matrix = [[0,0,1],[1,1,1],[1,0,1]]
输出: 4
解释: 重排后得到 [[1,1,0],[1,1,1],[1,1,0]]，全1子矩阵面积为4。
"""

from typing import List, Optional


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # 计算每列连续1的高度（从上方累积）
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        ans = 0
        for i in range(m):
            # 对当前行的高度排序（降序）
            row = sorted(matrix[i], reverse=True)
            for j in range(n):
                # 以 row[j] 为高，j+1 为宽的矩形
                ans = max(ans, row[j] * (j + 1))

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 对每一列，计算从上方累积的连续1的高度（类似柱状图）。
# 对于每一行，将高度降序排序。由于每行可以按任意顺序重排列，
# 排序后的高度序列表示：以 row[j] 为高，(j+1) 为宽的子矩阵全部为1。
# 最大面积 = max(row[j] * (j+1)) for each row。
#
# 时间复杂度: O(M * N log N) — 每行排序
# 空间复杂度: O(1) — 原地修改输入矩阵
#
# 关键点:
# - 列可以任意重排（每行独立），所以排序后能获得最大连续宽度
# - 问题转化为每行的 Largest Rectangle in Histogram 简化版
# - 排序后 row[j]*(j+1) 计算以该高度为限制的最大矩形
