"""
LeetCode #304 - Range Sum Query 2D - Immutable
中文题名：二维区域和检索 - 矩阵不可变
https://leetcode.com/problems/range-sum-query-2d-immutable/

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by
its upper left corner (row1, col1) and lower right corner (row2,
col2).

The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
[3, 0, 1, 4, 2],
[5, 6, 3, 2, 1],
[1, 2, 0, 1, 5],
[4, 1, 0, 1, 7],
[1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:

You may assume that the matrix does not change.

There are many calls to sumRegion function.

You may assume that row1 <= row2 and col1 <= col2.

【中文翻译】
给定一个二维矩阵 matrix，计算其子矩形范围内元素的总和，该子矩阵的
左上角为 (row1, col1)，右下角为 (row2, col2)。

上述矩形（红色边框）由 (row1, col1) = (2, 1) 和 (row2, col2) = (4, 3) 定义，其中包含的总和为 8。

示例：

给定 matrix = [
[3, 0, 1, 4, 2],
[5, 6, 3, 2, 1],
[1, 2, 0, 1, 5],
[4, 1, 0, 1, 7],
[1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

注意：

你可以假设矩阵不可变。

会多次调用 sumRegion 函数。

你可以假设 row1 <= row2 且 col1 <= col2。
"""

from typing import List, Optional


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.m, self.n = 0, 0
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.prefix[i + 1][j + 1] = (
                    self.prefix[i][j + 1]
                    + self.prefix[i + 1][j]
                    - self.prefix[i][j]
                    + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 二维前缀和。构建一个 (m+1) x (n+1) 的前缀和数组 prefix，
# 其中 prefix[i][j] 表示从 (0,0) 到 (i-1,j-1) 的矩形区域的和。
# 构造公式：prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1]
# 查询公式：sum = prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1]
# 查询 O(1) 通过容斥原理：大面积减去两个长方形再加回被重复减去的左上角。
#
# 时间复杂度: 构造 O(m*n)，每次查询 O(1)
# 空间复杂度: O(m*n)
#
# 关键点:
# - 二维前缀和通过容斥原理计算子矩阵和
# - prefix 数组多一行一列（m+1 x n+1）简化边界处理，避免判断 i==0 或 j==0
# - 查询公式中左上角被减了两次需要加回
