"""
LeetCode #1981 - Minimize the Difference Between Target and Chosen Elements
最小化目标值与所选元素的差
https://leetcode.cn/problems/minimize-the-difference-between-target-and-chosen-elements/

给你一个大小为 `m x n` 的整数矩阵 `mat` 和一个整数 `target` 。
从矩阵的 每一行 中选择一个整数，你的目标是 最小化 所有选中元素之 和 与目标值 `target` 的 绝对差 。
返回 最小的绝对差 。
`a` 和 `b` 两数字的 绝对差 是 `a - b` 的绝对值。

示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13 输出：0 解释：一种可能的最优选择方案是： - 第一行选出 1 - 第二行选出 5 - 第三行选出 7 所选元素的和是 13 ，等于目标值，所以绝对差是 0 。
示例 2：

输入：mat = [[1],[2],[3]], target = 100 输出：94 解释：唯一一种选择方案是： - 第一行选出 1 - 第二行选出 2 - 第三行选出 3 所选元素的和是 6 ，绝对差是 94 。
示例 3：

输入：mat = [[1,2,9,8,7]], target = 6 输出：1 解释：最优的选择方案是选出第一行的 7 。 绝对差是 1 。

提示：
`m == mat.length`
`n == mat[i].length`
`1 <= m, n <= 70`
`1 <= mat[i][j] <= 70`
`1 <= target <= 800`
"""

from typing import List, Optional


class Solution:
    def minimizeTheDifference(
        self, mat: List[List[int]], target: int
    ) -> int:
        """
        DP with bitset: track all possible sums row by row.
        Each cell value is small (<= 70), max sum <= m * 70 = 4900.
        Use a bitset (int as bitmask) to represent reachable sums.
        """
        max_sum = 70 * 70  # m,n <= 70, max val <= 70 -> max sum = 4900
        dp = 1  # bit 0 is set (sum 0 is reachable initially)

        for row in mat:
            # Deduplicate values in the row
            unique_vals = set(row)
            next_dp = 0
            for val in unique_vals:
                next_dp |= dp << val
            dp = next_dp

        # Find the sum closest to target
        best = float("inf")
        for s in range(max_sum + 1):
            if (dp >> s) & 1:
                diff = abs(s - target)
                if diff < best:
                    best = diff

        return best



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Matrix
#
# 解题思路:
# 使用位运算优化的 DP（bitset）。dp 用一个整数的二进制位表示哪些和是可达的。
# 初始 dp = 1（只有和为 0 可达）。
# 对于每一行，对去重后的每个值 val，next_dp |= dp << val，
# 表示将之前的每个可达和加上 val 变成新的可达和。
# 所有行处理完后，扫描所有可达的和，找到与 target 最接近的。
# 由于 max_sum <= 4900（70*70），单次移位和或运算非常高效。
#
# 时间复杂度: O(M * unique_vals_per_row * max_sum/64 + max_sum)，bitset 运算
# 空间复杂度: O(1)，只用一个整数表示状态
#
# 关键点:
# - bitset DP：用整数的位表示可达和
# - 每行先去重减少计算量
# - 值和范围小 (<=70)，使得 bitset 长度可控
