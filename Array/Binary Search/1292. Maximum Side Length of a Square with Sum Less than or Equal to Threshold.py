"""
LeetCode #1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
中文题名：元素和小于等于阈值的正方形的最大边长
https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

Given a `m x n` matrix `mat` and an integer `threshold`.
Return the maximum side-length of a square with a sum less than or equal to `threshold`
or return 0 if there is no such square.

Example 1:

Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0

Example 3:

Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3

Example 4:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2

Constraints:

`1 <= m, n <= 300`

`m == mat.length`

`n == mat[i].length`

`0 <= mat[i][j] <= 10000`

`0 <= threshold <= 10^5`

【中文翻译】
给定一个 m x n 的矩阵 mat 和一个整数 threshold。返回元素和小于或等于 threshold 的正方形的最大边长，如果不存在这样的正方形则返回 0。

示例 1：

输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
输出：2
解释：元素和小于等于 4 的正方形的最大边长为 2，如图所示。

示例 2：

输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
输出：0

示例 3：

输入：mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
输出：3

示例 4：

输入：mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
输出：2

约束条件：

1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold <= 10^5
"""

from typing import List, Optional


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Build 2D prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    prefix[i][j + 1] + prefix[i + 1][j]
                    - prefix[i][j] + mat[i][j]
                )

        def square_sum(r: int, c: int, side: int) -> int:
            """Sum of square with top-left at (r, c) and given side length."""
            r2, c2 = r + side - 1, c + side - 1
            return (
                prefix[r2 + 1][c2 + 1]
                - prefix[r][c2 + 1]
                - prefix[r2 + 1][c]
                + prefix[r][c]
            )

        def has_square(side: int) -> bool:
            """Check if there exists a square of given side length with sum <= threshold."""
            for i in range(m - side + 1):
                for j in range(n - side + 1):
                    if square_sum(i, j, side) <= threshold:
                        return True
            return False

        left, right = 1, min(m, n)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if has_square(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用二维前缀和 + 二分查找。
# 1. 构建二维前缀和数组 prefix，prefix[i+1][j+1] 表示从 (0,0) 到 (i,j) 的矩形区域和。
#    公式：prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + mat[i][j]
# 2. 使用前缀和可以在 O(1) 时间内计算任意正方形区域的和。
# 3. 对边长进行二分查找（范围 [1, min(m, n)]）：
#    - 检查是否存在边长为 mid 的正方形其和 <= threshold
#    - 若存在，尝试更大的边长；若不存在，尝试更小的边长
# 4. 返回找到的最大边长。
#
# 时间复杂度: O(m*n*log(min(m,n))) - 二分查找 O(log min(m,n))，每次检查 O(m*n)
# 空间复杂度: O(m*n) - 前缀和数组
#
# 关键点:
# - 二维前缀和快速计算任意子矩阵和：sum = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
# - 二分查找正方形的边长而非逐个枚举，效率更高
# - 前缀和数组多一行一列便于边界处理
