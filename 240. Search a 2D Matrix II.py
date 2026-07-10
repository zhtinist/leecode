"""
LeetCode #240 - Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This
matrix has the following properties:

Integers in each row are sorted in ascending from left to right.

Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
[1,   4,  7, 11, 15],
[2,   5,  8, 12, 19],
[3,   6,  9, 16, 22],
[10, 13, 14, 17, 24],
[18, 21, 23, 26, 30]
]

Given target = `5`, return `true`.

Given target = `20`, return `false`.
"""

from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 从右上角开始搜索，利用矩阵的行列有序性。
# 矩阵性质：每行从左到右递增，每列从上到下递增。
# 从右上角 matrix[0][cols-1] 开始：
# - 如果当前元素 == target，找到目标，返回 True。
# - 如果当前元素 < target，说明当前行左边的所有元素都更小，
#   因为每行递增，target 不可能在当前行，向下移动一行(row += 1)。
# - 如果当前元素 > target，说明当前列下方的所有元素都更大，
#   因为每列递增，target 不可能在当前列，向左移动一列(col -= 1)。
# 每次比较可以排除一行或一列，最多 m + n 次比较。
# 类似地，也可以从左下角开始(向下/向右)。
#
# 时间复杂度: O(m + n) - 每次排除一行或一列，最多 m+n 步
# 空间复杂度: O(1) - 只使用行列指针
#
# 关键点:
# - 右上角(或左下角)是"行列有序性"的分界点：往左变小，往下变大
# - 不要从左上角或右下角开始(两边同时大或同时小，无法决策)
# - 这是减治法(Decrease and Conquer)的典型应用
# - 比二分查找更优的二维搜索方式，充分利用了两个维度的有序性
