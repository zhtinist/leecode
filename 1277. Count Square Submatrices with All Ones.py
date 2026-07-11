"""
LeetCode #1277 - Count Square Submatrices with All Ones
中文题名：统计全为 1 的正方形子矩阵
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Given a `m * n` matrix of ones and zeros, return how many
square submatrices have all ones.

Example 1:

Input: matrix =
[
[0,1,1,1],
[1,1,1,1],
[0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix =
[
[1,0,1],
[1,1,0],
[1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

Constraints:

`1 <= arr.length <= 300`

`1 <= arr[0].length <= 300`

`0 <= arr[i][j] <= 1`

【中文翻译】
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1。返回其中完全由 1 组成的正方形子矩阵的个数。

示例 1：

输入：matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
输出：15
解释：
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15。

示例 2：

输入：matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7。

约束条件：

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""

from typing import List, Optional


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    total += dp[i][j]

        return total










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划。定义 dp[i][j] 表示以 (i, j) 为右下角的最大全1正方形的边长。
# 若 matrix[i][j] == 1：
#   - 当 i == 0 或 j == 0 时，dp[i][j] = 1（边界上只能形成边长为1的正方形）
#   - 否则 dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#     含义：以 (i, j) 为右下角的正方形最大边长，取决于其上方、左方和左上方
#     三个位置能形成的正方形的最小边长，再加上当前格子本身。
# 最终将所有 dp[i][j] 的值累加即为答案，因为 dp[i][j] 的值恰好等于
# 以 (i, j) 为右下角的不同边长正方形的个数。
#
# 时间复杂度: O(m*n) - 需要遍历矩阵中的每个元素
# 空间复杂度: O(m*n) - dp 数组大小与输入矩阵相同（可优化为 O(n)）
#
# 关键点:
# - dp[i][j] 既表示最大正方形边长，又表示以该位置为右下角的正方形个数
# - 状态转移依赖左、上、左上三个方向，因此从左上到右下遍历
# - 可以原地修改 matrix 将空间优化至 O(1)
