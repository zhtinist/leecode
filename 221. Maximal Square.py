"""
LeetCode #221 - Maximal Square
https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing
only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

from typing import List, Optional


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side












# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划(DP)。
# 定义 dp[i][j] 表示以 matrix[i-1][j-1] 为右下角的最大正方形边长。
# 状态转移方程：
#   若 matrix[i-1][j-1] == '1'：
#     dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#   否则 dp[i][j] = 0。
# 解释：以当前格子为右下角的正方形，其最大边长受限于左方、上方和左上方
# 三个方向的最大正方形边长中的最小值 + 1。
# 最终答案为 max(dp[i][j]) 的平方(面积)。
#
# 时间复杂度: O(m * n) - 遍历矩阵中每个元素
# 空间复杂度: O(m * n) - DP 数组大小，可优化至 O(n) 只保留上一行
#
# 关键点:
# - dp 数组比原矩阵多一行一列，避免边界判断
# - dp[i][j] 的取值由左、上、左上三个方向的最小值决定
# - 最终返回边长的平方(面积)而非边长本身
