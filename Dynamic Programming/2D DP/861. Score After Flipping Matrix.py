"""
LeetCode #861 - Score After Flipping Matrix
中文题名：翻转矩阵后的得分
https://leetcode.com/problems/score-after-flipping-matrix/

We have a two dimensional matrix `A` where each value is `0` or
`1`.

A move consists of choosing any row or column, and toggling each value in that row or column:
changing all `0`s to `1`s, and all `1`s to `0`s.

After making any number of moves, every row of this matrix is interpreted as a binary number,
and the score of the matrix is the sum of these numbers.

Return the highest possible score.

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:

`1 <= A.length <= 20`

`1 <= A[0].length <= 20`

`A[i][j]` is `0` or `1`.

【中文翻译】
我们有一个二维矩阵 A，其中每个值为 0 或 1。

一次操作包括选择任意一行或一列，并翻转该行或列中的每个值：将所有 0 变为 1，所有 1 变为 0。

在进行任意次操作后，将矩阵的每一行解释为一个二进制数，矩阵的得分是这些数的和。

返回可能的最高得分。

"""

from typing import List, Optional


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Step 1: Flip rows so that the first column is all 1s
        # A leading 1 contributes 2^(n-1) to the row sum
        # This is always worth it (greedy for MSB)
        for i in range(m):
            if grid[i][0] == 0:
                # Flip this row
                for j in range(n):
                    grid[i][j] ^= 1

        # Step 2: For each remaining column, if it has more 0s than 1s, flip it
        # The contribution of column j is: count_of_1s * 2^(n-1-j)
        result = m * (1 << (n - 1))  # First column: all are 1 after step 1

        for j in range(1, n):
            ones = sum(grid[i][j] for i in range(m))
            ones = max(ones, m - ones)  # Take max after potential column flip
            result += ones * (1 << (n - 1 - j))

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略，分两步：
# 第一步：确保每行的最高位（第一列）全为 1。
# 因为第一列的贡献是 2^(n-1)，是所有列中最大的。
# 对于第一列为 0 的行，翻转整行使其变为 1。这个操作永远值得做。
#
# 第二步：从第二列开始，对于每一列，统计其中 1 的数量。
# 如果某列中 1 的数量少于 0 的数量，翻转该列。
# 因为翻转一列不会影响其他列的 1/0 分布（只影响当前列），
# 让每列中 1 尽可能多就能最大化总和。
# 注意：实际实现时不需要真的翻转列，只需统计 max(ones, m-ones)。
#
# 时间复杂度: O(M * N)
# 空间复杂度: O(1)
#
# 关键点:
# - 贪心策略分两步，先保证最高位（第一列）全为 1，再逐列优化
# - 第一列的贡献 2^(n-1) 大于其余所有列贡献之和，因此必须保证第一列为 1
# - 后续每列独立决策：1 多就保持，0 多就翻转（统计 max(ones, m-ones)）
# - 使用位运算 1 << (n-1-j) 计算每列的权重
