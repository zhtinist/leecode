"""
LeetCode #2536 - Increment Submatrices by One
子矩阵元素加 1
https://leetcode.cn/problems/increment-submatrices-by-one/

给你一个正整数 `n` ，表示最初有一个 `n x n` 、下标从 0 开始的整数矩阵 `mat` ，矩阵中填满了 0 。
另给你一个二维整数数组 `query` 。针对每个查询 `query[i] = [row1_i, col1_i, row2_i, col2_i]` ，请你执行下述操作：
找出 左上角 为 `(row1_i, col1_i)` 且 右下角 为 `(row2_i, col2_i)` 的子矩阵，将子矩阵中的 每个元素 加 `1` 。也就是给所有满足 `row1_i <= x <= row2_i` 和 `col1_i <= y <= col2_i` 的 `mat[x][y]` 加 `1` 。
返回执行完所有操作后得到的矩阵 `mat` 。

示例 1：

输入：n = 3, queries = [[1,1,2,2],[0,0,1,1]] 输出：[[1,1,0],[1,2,1],[0,1,1]] 解释：上图所展示的分别是：初始矩阵、执行完第一个操作后的矩阵、执行完第二个操作后的矩阵。 - 第一个操作：将左上角为 (1, 1) 且右下角为 (2, 2) 的子矩阵中的每个元素加 1 。  - 第二个操作：将左上角为 (0, 0) 且右下角为 (1, 1) 的子矩阵中的每个元素加 1 。
示例 2：

输入：n = 2, queries = [[0,0,1,1]] 输出：[[1,1],[1,1]] 解释：上图所展示的分别是：初始矩阵、执行完第一个操作后的矩阵。  - 第一个操作：将矩阵中的每个元素加 1 。

提示：
`1 <= n <= 500`
`1 <= queries.length <= 10^4`
`0 <= row1_i <= row2_i < n`
`0 <= col1_i <= col2_i < n`
"""

from typing import List, Optional


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                mat[i][j] = diff[i][j]
                if i > 0:
                    mat[i][j] += mat[i - 1][j]
                if j > 0:
                    mat[i][j] += mat[i][j - 1]
                if i > 0 and j > 0:
                    mat[i][j] -= mat[i - 1][j - 1]
        return mat



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Prefix Sum
#
# 解题思路:
# 使用二维差分数组。对每个查询[r1,c1,r2,c2]，在diff[r1][c1]处+1，diff[r1][c2+1]处-1，
# diff[r2+1][c1]处-1，diff[r2+1][c2+1]处+1。最后对差分数组做二维前缀和得到最终矩阵。
#
# 时间复杂度: O(Q + N^2)，Q为查询数
# 空间复杂度: O(N^2)
#
# 关键点:
# - 二维差分将区间更新从O(N^2)降到O(1)每次查询
# - 差分数组比原矩阵多一行一列，简化边界处理
# - 前缀和还原时注意重复加/减的区域
