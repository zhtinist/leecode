"""
LeetCode #279 - Perfect Squares
中文题名：完全平方数
https://leetcode.com/problems/perfect-squares/

Given a positive integer *n*, find the least number of perfect square numbers (for
example, `1, 4, 9, 16, ...`) which sum to *n*.

Example 1:

Input: *n* = `12`
Output: 3
Explanation: `12 = 4 + 4 + 4.`

Example 2:

Input: *n* = `13`
Output: 2
Explanation: `13 = 4 + 9.`

【中文翻译】
给定一个正整数 *n*，找到最少需要多少个完全平方数（例如 `1, 4, 9, 16, ...`）使其和等于 *n*。

示例 1：

输入：*n* = `12`
输出：3
解释：`12 = 4 + 4 + 4.`

示例 2：

输入：*n* = `13`
输出：2
解释：`13 = 4 + 9.`
"""

from typing import List, Optional


class Solution:
    def numSquares(self, n: int) -> int:
        """Find the least number of perfect square numbers that sum to n.

        DP approach: dp[i] = minimum number of perfect squares summing to i.
        For each i, try subtracting every perfect square j*j <= i.
        dp[i] = min(dp[i], dp[i - j*j] + 1)
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        # Pre-compute all square numbers <= n
        squares = []
        j = 1
        while j * j <= n:
            squares.append(j * j)
            j += 1

        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。定义 dp[i] 为组成数字 i 所需的最少完全平方数个数。
# 对于每个 i，尝试减去所有可能的完全平方数 j*j（j*j <= i），
# 取 dp[i - j*j] + 1 的最小值。
# 初始化 dp[0] = 0，其余为无穷大。
# 也可以使用 BFS（把每个数字看作图节点，减去平方数作为边）或者
# 拉格朗日四平方定理（但需要额外处理）。
#
# 时间复杂度: O(N * sqrt(N)) - 外层 N，内层最多 sqrt(N) 个平方数
# 空间复杂度: O(N) - dp 数组大小 N+1
#
# 关键点:
# - dp[0] = 0 是基础情况
# - 内层循环只需要遍历平方数 <= i 的部分
# - 可以预先计算所有平方数列表
# - 另一种更优解法: BFS 或 数学方法（四平方定理）
