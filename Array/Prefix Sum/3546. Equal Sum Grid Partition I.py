"""
LeetCode #3546 - Equal Sum Grid Partition I
等和矩阵分割 I
https://leetcode.cn/problems/equal-sum-grid-partition-i/

给你一个由正整数组成的 `m x n` 矩阵 `grid`。你的任务是判断是否可以通过 一条水平或一条垂直分割线 将矩阵分割成两部分，使得：
分割后形成的每个部分都是 非空 的。
两个部分中所有元素的和 相等 。
如果存在这样的分割，返回 `true`；否则，返回 `false`。

示例 1：

输入： grid = [[1,4],[2,3]]
输出： true
解释：

在第 0 行和第 1 行之间进行水平分割，得到两个非空部分，每部分的元素之和为 5。因此，答案是 `true`。
示例 2：

输入： grid = [[1,3],[2,4]]
输出： false
解释：
无论是水平分割还是垂直分割，都无法使两个非空部分的元素之和相等。因此，答案是 `false`。

提示：
`1 <= m == grid.length <= 10^5`
`1 <= n == grid[i].length <= 10^5`
`2 <= m * n <= 10^5`
`1 <= grid[i][j] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def equalSumGridPartition(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        if total % 2 != 0:
            return False  # total must be even for equal split

        target = total // 2

        # Check horizontal splits (between rows)
        row_sum = 0
        for i in range(m - 1):
            row_sum += sum(grid[i])
            if row_sum == target:
                return True

        # Check vertical splits (between columns)
        col_sum = 0
        for j in range(n - 1):
            col_sum += sum(grid[i][j] for i in range(m))
            if col_sum == target:
                return True

        return False










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Enumeration, Matrix, Prefix Sum
#
# 解题思路:
# 计算整个矩阵的总和 total。如果 total 不是偶数，不可能分成两个和相等的部分，直接返回 false。
# 水平分割：逐行累加行和，如果某一行之后的行和等于 total/2，说明上半部分和等于下半部分和，返回 true。
# 垂直分割：逐列累加列和，如果某一列之后的列和等于 total/2，说明左半部分和等于右半部分和，返回 true。
# 两者都找不到则返回 false。注意行和列都至少保留一个非空部分，所以循环到 m-1 和 n-1。
#
# 时间复杂度: O(m * n)，需要遍历整个矩阵一次计算总和，再遍历一次检查行列累加和。
# 空间复杂度: O(1)，只使用常数个变量。
#
# 关键点:
# - 总和必须为偶数，才能分成两个和相等的部分。
# - 水平分割只需检查行累加和，垂直分割只需检查列累加和。
# - 两种分割互不影响，找到任意一种即可返回 true。
