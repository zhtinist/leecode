"""
LeetCode #1314 - Matrix Block Sum
中文题名：矩阵区域和
https://leetcode.com/problems/matrix-block-sum/

Given a `m * n` matrix `mat` and an integer
`K`, return a matrix `answer` where each `answer[i][j]` is
the sum of all elements `mat[r][c]` for `i - K <= r <= i + K, j -
K <= c <= j + K`, and `(r, c)` is a valid position in the
matrix.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]

Constraints:

`m == mat.length`

`n == mat[i].length`

`1 <= m, n, K <= 100`

`1 <= mat[i][j] <= 100`

【中文翻译】
给定一个 m * n 的矩阵 mat 和一个整数 K，返回一个矩阵 answer，
其中每个 answer[i][j] 是所有满足 i - K <= r <= i + K, j - K <= c <= j + K
且 (r, c) 在矩阵中的有效位置的 mat[r][c] 之和。

示例 1：
输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]

示例 2：
输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]

约束条件：
m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # Build 2D prefix sum: prefix[i+1][j+1] = sum of submatrix (0,0) to (i,j)
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        # Compute answer using prefix sum
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # Top-left and bottom-right corners of the block (clamped to matrix bounds)
                r1 = max(0, i - K)
                c1 = max(0, j - K)
                r2 = min(m - 1, i + K)
                c2 = min(n - 1, j + K)

                # Block sum via inclusion-exclusion
                answer[i][j] = (
                    prefix[r2 + 1][c2 + 1]
                    - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    + prefix[r1][c1]
                )
        return answer



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用二维前缀和（2D Prefix Sum）技巧。
# 1. 构建前缀和矩阵 prefix，其中 prefix[i+1][j+1] 表示从 (0,0) 到 (i,j) 的子矩阵元素之和。
#    递推公式：prefix[i+1][j+1] = mat[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
# 2. 对于每个位置 (i,j)，确定其 K-邻域块的四个边界：
#    r1 = max(0, i-K), c1 = max(0, j-K), r2 = min(m-1, i+K), c2 = min(n-1, j+K)
# 3. 使用容斥原理计算该块的和：
#    sum = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
# 这样每个 answer[i][j] 只需 O(1) 时间计算。
#
# 时间复杂度: O(M * N)，构建前缀和 O(M*N)，计算答案 O(M*N)
# 空间复杂度: O(M * N)，前缀和矩阵大小 (M+1)*(N+1)，答案矩阵 O(M*N)（不计入额外空间）
#
# 关键点:
# - 二维前缀和的容斥原理公式
# - 使用 (M+1)*(N+1) 大小的前缀矩阵，第一行/列为 0，简化边界处理
# - r1/r2/c1/c2 的边界裁剪确保不越界
# - 类似题目：304. Range Sum Query 2D - Immutable（矩形区域和检索）
# - 如果不使用前缀和，每个位置需要 O(K^2) 时间，会超时










