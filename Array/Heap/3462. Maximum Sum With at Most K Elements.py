"""
LeetCode #3462 - Maximum Sum With at Most K Elements
提取至多 K 个元素的最大总和
https://leetcode.cn/problems/maximum-sum-with-at-most-k-elements/

给你一个大小为 `n x m` 的二维矩阵 `grid` ，以及一个长度为 `n` 的整数数组 `limits` ，和一个整数 `k` 。你的目标是从矩阵 `grid` 中提取出 至多 `k` 个元素，并计算这些元素的最大总和，提取时需满足以下限制：

从 `grid` 的第 `i` 行提取的元素数量不超过 `limits[i]` 。
返回最大总和。

示例 1：

输入：grid = [[1,2],[3,4]], limits = [1,2], k = 2
输出：7
解释：
从第 2 行提取至多 2 个元素，取出 4 和 3 。
至多提取 2 个元素时的最大总和 `4 + 3 = 7` 。
示例 2：

输入：grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3
输出：21
解释：
从第 1 行提取至多 2 个元素，取出 7 。
从第 2 行提取至多 2 个元素，取出 8 和 6 。
至多提取 3 个元素时的最大总和 `7 + 8 + 6 = 21` 。

提示：
`n == grid.length == limits.length`
`m == grid[i].length`
`1 <= n, m <= 500`
`0 <= grid[i][j] <= 10^5`
`0 <= limits[i] <= m`
`0 <= k <= min(n * m, sum(limits))`
"""

from typing import List, Optional


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        for row, limit in zip(grid, limits):
            row_sorted = sorted(row, reverse=True)
            candidates.extend(row_sorted[:limit])
        candidates.sort(reverse=True)
        return sum(candidates[:k])



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Matrix, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 1. 对每一行降序排列，取前 limits[i] 个最大值作为该行的候选元素
# 2. 将所有行的候选元素合并到一个列表中
# 3. 对候选列表降序排列，取前 k 个元素求和
# 4. 贪心策略：每一行内部取最大的元素，再全局取最大的 k 个
#
# 时间复杂度: O(n * m log m + total * log(total))
# 空间复杂度: O(total) 其中 total = sum(limits)
#
# 关键点:
# - 每一行内部的元素选取受 limits[i] 限制，先取每行最大
# - 全局再选最大的 k 个，保证总和最大
