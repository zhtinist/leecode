"""
LeetCode #931 - Minimum Falling Path Sum
中文题名：下降路径最小和
https://leetcode.com/problems/minimum-falling-path-sum/

Given a square array of integers `A`, we want the
minimum sum of a falling path through `A`.

A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's
column by at most one.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:

`[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]`

`[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]`

`[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]`

The falling path with the smallest sum is `[1,4,7]`, so the answer is
`12`.

Note:

`1 <= A.length == A[0].length <= 100`

`-100 <= A[i][j] <= 100`

【中文翻译】

给定一个整数方阵 A，我们想要找到通过 A 的下降路径的最小和。
下降路径从第一行的任意元素开始，并从每一行选择一个元素。
下一行选择的元素所在的列必须与上一行选择的列相差至多 1。

"""

from typing import List, Optional


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        In-place DP: for each row from top to bottom,
        update matrix[i][j] += min(above-left, above, above-right).
        """
        n = len(matrix)

        for i in range(1, n):
            for j in range(n):
                # Minimum of the three cells above
                above = matrix[i - 1][j]
                if j > 0:
                    above = min(above, matrix[i - 1][j - 1])
                if j < n - 1:
                    above = min(above, matrix[i - 1][j + 1])
                matrix[i][j] += above

        return min(matrix[-1])



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划（原地修改矩阵）：
# 从第二行开始，对于每个位置 (i, j)，更新为：
# matrix[i][j] += min(matrix[i-1][j-1]（若 j>0）, matrix[i-1][j], matrix[i-1][j+1]（若 j<n-1）)
# 即当前格子的值加上上一行三个相邻位置的最小值。
# 最后返回最后一行的最小值即可。
#
# 时间复杂度: O(N^2)，其中 N 是矩阵边长
# 空间复杂度: O(1)（原地修改输入矩阵）
#
# 关键点:
# - 经典的二维 DP，类似三角形最小路径和
# - 每个位置可以从左上方、正上方、右上方转移而来
# - 注意边界条件：第一列没有左上方，最后一列没有右上方
