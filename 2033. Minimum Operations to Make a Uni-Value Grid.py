"""
LeetCode #2033 - Minimum Operations to Make a Uni-Value Grid
获取单值网格的最小操作数
https://leetcode.cn/problems/minimum-operations-to-make-a-uni-value-grid/

给你一个大小为 `m x n` 的二维整数网格 `grid` 和一个整数 `x` 。每一次操作，你可以对 `grid` 中的任一元素 加 `x` 或 减 `x` 。
单值网格 是全部元素都相等的网格。
返回使网格化为单值网格所需的 最小 操作数。如果不能，返回 `-1` 。

示例 1：

输入：grid = [[2,4],[6,8]], x = 2 输出：4 解释：可以执行下述操作使所有元素都等于 4 ：  - 2 加 x 一次。 - 6 减 x 一次。 - 8 减 x 两次。 共计 4 次操作。
示例 2：

输入：grid = [[1,5],[2,3]], x = 1 输出：5 解释：可以使所有元素都等于 3 。
示例 3：

输入：grid = [[1,2],[3,4]], x = 2 输出：-1 解释：无法使所有元素相等。

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 10^5`
`1 <= m * n <= 10^5`
`1 <= x, grid[i][j] <= 10^4`
"""

from typing import List, Optional


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid
        nums = [v for row in grid for v in row]
        nums.sort()

        # Check if all elements have the same remainder mod x
        remainder = nums[0] % x
        for v in nums:
            if v % x != remainder:
                return -1

        # Make all elements equal to the median
        median = nums[len(nums) // 2]
        operations = sum(abs(v - median) // x for v in nums)
        return operations



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Matrix, Sorting
#
# 解题思路:
# 将二维网格展平为一维数组。检查所有元素对x取模的余数是否相同，
# 如果不同则不可能变成单值网格（因为加减x不改变模x的余数）。
# 将所有元素变成中位数需要的操作数最少（绝对值之和最小化的性质）。
# 操作数 = sum(|v - median| / x)。
#
# 时间复杂度: O(m·n·log(m·n))
# 空间复杂度: O(m·n)
#
# 关键点:
# - 模x的余数一致性检查
# - 中位数是最优目标值
# - 操作次数 = 差值除以x
