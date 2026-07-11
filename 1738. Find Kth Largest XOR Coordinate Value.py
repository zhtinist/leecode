"""
LeetCode #1738 - Find Kth Largest XOR Coordinate Value
中文题名：找出第 K 大的异或坐标值
https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

You are given a 2D `matrix` of size `m x n`, consisting of
non-negative integers. You are also given an integer `k`.

The value of coordinate `(a, b)` of the matrix is the XOR
of all `matrix[i][j]` where `0 <= i <= a < m` and
`0 <= j <= b < n` (0-indexed).

Find the `kth` largest value (1-indexed) of
all the coordinates of `matrix`.

Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.

Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.

Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.

Example 4:

Input: matrix = [[5,2],[1,6]], k = 4
Output: 0
Explanation: The value of coordinate (1,1) is 5 XOR 2 XOR 1 XOR 6 = 0, which is the 4th largest value.

Constraints:

`m == matrix.length`

`n == matrix[i].length`

`1 <= m, n <= 1000`

`0 <= matrix[i][j] <= 106`

`1 <= k <= m * n`

【中文翻译】
给定一个 m x n 的矩阵 matrix。定义坐标 (a, b) 的值为 matrix[0][0] 到 matrix[a][b] 子矩阵中所有元素的异或结果。
找出所有坐标值中第 k 大的值（k 从1开始）。

示例 1：
输入: matrix = [[5,2],[1,6]], k = 1
输出: 7
解释: (0,0)=5, (0,1)=5^2=7, (1,0)=5^1=4, (1,1)=5^2^1^6=2。第1大是7。
"""

from typing import List, Optional


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor_values = []

        # 2D 前缀异或
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                if i > 0:
                    val ^= dp[i - 1][j]
                if j > 0:
                    val ^= dp[i][j - 1]
                if i > 0 and j > 0:
                    val ^= dp[i - 1][j - 1]
                dp[i][j] = val
                xor_values.append(val)

        xor_values.sort(reverse=True)
        return xor_values[k - 1]
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 二维前缀异或。定义 dp[i][j] = matrix[0..i][0..j] 的异或值。
# 递推公式：dp[i][j] = matrix[i][j] ^ dp[i-1][j] ^ dp[i][j-1] ^ dp[i-1][j-1]。
# （异或的逆运算仍是异或，所以加法和减法的前缀和公式直接适用）
# 收集所有坐标值，降序排序，返回第 k 个。
#
# 时间复杂度: O(M * N * log(M*N)) — 生成前缀异或 + 排序
# 空间复杂度: O(M * N) — 存储前缀异或和所有值
#
# 关键点:
# - 异或的性质：a ^ a = 0，a ^ 0 = a
# - 前缀异或公式与前缀和公式相同（异或即加法也是减法）
# - 注意去重：dp[i-1][j-1] 需要异或回来（因为被减了两次）
