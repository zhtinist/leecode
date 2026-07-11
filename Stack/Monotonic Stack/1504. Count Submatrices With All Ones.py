"""
LeetCode #1504 - Count Submatrices With All Ones
中文题名：统计全 1 子矩形
https://leetcode.com/problems/count-submatrices-with-all-ones/

Given a `rows * columns` matrix `mat` of ones and
zeros, return how many submatrices have all ones.

Example 1:

Input: mat = [[1,0,1],
[1,1,0],
[1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2.
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

Example 2:

Input: mat = [[0,1,1,0],
[0,1,1,1],
[1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3.
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2.
There are 2 rectangles of side 3x1.
There is 1 rectangle of side 3x2.
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.

Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21

Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5

Constraints:

`1 <= rows <= 150`

`1 <= columns <= 150`

`0 <= mat[i][j] <= 1`

【中文翻译】
给定一个由 0 和 1 组成的 rows*columns 矩阵 mat，返回其中全为 1 的子矩形数量。

示例 1：

输入：mat = [[1,0,1],[1,1,0],[1,1,0]]
输出：13
解释：有 6 个 1x1 矩形，2 个 1x2 矩形，3 个 2x1 矩形，1 个 2x2 矩形，1 个 3x1 矩形。
共 6+2+3+1+1=13。

示例 2：

输入：mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
输出：24

示例 3：

输入：mat = [[1,1,1,1,1,1]]
输出：21

示例 4：

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5
"""

from typing import List, Optional


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # heights[j] = consecutive 1s ending at current row in column j
        heights = [0] * n
        result = 0
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            # Count submatrices ending at row i
            for j in range(n):
                min_height = heights[j]
                for k in range(j, -1, -1):
                    min_height = min(min_height, heights[k])
                    if min_height == 0:
                        break
                    result += min_height
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 逐行处理，维护 heights 数组表示当前行每列向上连续 1 的个数（直方图高度）。
# 对于每一行，以每个位置 (i,j) 为右下角，向左扩展，维护最小高度 min_h。
# 以 (i,j) 为右下角、高度为 min_h 的子矩形数量 = min_h。
# 使用单调栈可以优化到 O(M*N)，但 O(M*N^2) 在约束范围内（150*150=22500）也足够。
#
# 时间复杂度: O(M * N^2)
# 空间复杂度: O(N)
#
# 关键点:
# - 转化为直方图问题：每行维护向上连续的 1 的高度
# - 以每个位置为右下角，向左扩展统计可形成的矩形数
# - 当前能形成的矩形高度由向左扩展过程中的最小高度决定
