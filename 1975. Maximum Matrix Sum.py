"""
LeetCode #1975 - Maximum Matrix Sum
最大方阵和
https://leetcode.cn/problems/maximum-matrix-sum/

给你一个 `n x n` 的整数方阵 `matrix` 。你可以执行以下操作 任意次 ：
选择 `matrix` 中 相邻 两个元素，并将它们都 乘以 `-1` 。
如果两个元素有 公共边 ，那么它们就是 相邻 的。
你的目的是 最大化 方阵元素的和。请你在执行以上操作之后，返回方阵的 最大 和。

示例 1：
输入：matrix = [[1,-1],[-1,1]] 输出：4 解释：我们可以执行以下操作使和等于 4 ： - 将第一行的 2 个元素乘以 -1 。 - 将第一列的 2 个元素乘以 -1 。
示例 2：
输入：matrix = [[1,2,3],[-1,-2,-3],[1,2,3]] 输出：16 解释：我们可以执行以下操作使和等于 16 ： - 将第二行的最后 2 个元素乘以 -1 。

提示：
`n == matrix.length == matrix[i].length`
`2 <= n <= 250`
`-10^5 <= matrix[i][j] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        We can flip any two adjacent elements. This means we can flip
        any pair of negative numbers to positive. If there are an even
        number of negatives, all can become positive. If odd, one stays
        negative — choose the one with smallest absolute value.
        """
        n = len(matrix)
        total = 0
        min_abs = float("inf")
        neg_count = 0

        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                if val < 0:
                    neg_count += 1
                abs_val = abs(val)
                total += abs_val
                if abs_val < min_abs:
                    min_abs = abs_val

        if neg_count % 2 == 1:
            # One negative must remain; make it the smallest absolute value
            total -= 2 * min_abs

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Matrix
#
# 解题思路:
# 操作允许同时翻转两个相邻元素的符号。这意味着负数可以沿着相邻路径"传播"。
# 两两配对翻转可以将两个负数同时变为正数。
# 如果负数个数为偶数，全部可以变为正数，答案为所有绝对值之和。
# 如果负数个数为奇数，必须保留一个负数，最优是让绝对值最小的那个数为负。
# 答案 = 所有绝对值之和 - 2 * 最小绝对值（如果负数个数为奇数）。
#
# 时间复杂度: O(N^2)，遍历矩阵
# 空间复杂度: O(1)
#
# 关键点:
# - 相邻翻转可以传播负号到任意位置
# - 偶数个负数可以全部变正
# - 奇数个负数留下绝对值最小的那个
