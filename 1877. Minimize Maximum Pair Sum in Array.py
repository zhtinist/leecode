"""
LeetCode #1877 - Minimize Maximum Pair Sum in Array
数组中最大数对和的最小值
https://leetcode.cn/problems/minimize-maximum-pair-sum-in-array/

一个数对 `(a,b)` 的 数对和 等于 `a + b` 。最大数对和 是一个数对数组中最大的 数对和 。
比方说，如果我们有数对 `(1,5)` ，`(2,3)` 和 `(4,4)`，最大数对和 为 `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8` 。
给你一个长度为 偶数 `n` 的数组 `nums` ，请你将 `nums` 中的元素分成 `n / 2` 个数对，使得：
`nums` 中每个元素 恰好 在 一个 数对中，且
最大数对和 的值 最小 。
请你在最优数对划分的方案下，返回最小的 最大数对和 。

示例 1：
输入：nums = [3,5,2,3] 输出：7 解释：数组中的元素可以分为数对 (3,3) 和 (5,2) 。 最大数对和为 max(3+3, 5+2) = max(6, 7) = 7 。
示例 2：
输入：nums = [3,5,4,2,4,6] 输出：8 解释：数组中的元素可以分为数对 (3,5)，(4,4) 和 (6,2) 。 最大数对和为 max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8 。

提示：
`n == nums.length`
`2 <= n <= 10^5`
`n` 是 偶数 。
`1 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = 0
        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[n - 1 - i])
        return max_sum



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Two Pointers, Sorting
#
# 解题思路:
# 贪心策略：排序后，将最小元素与最大元素配对。
# 证明：假设有两对 (a, b) 和 (c, d) 其中 a <= c <= d <= b，
# 则 max(a+b, c+d) >= max(a+d, c+b)，所以将最小与最大配对
# 可以使最大数对和最小化。
# 排序后双指针从两端向中间配对，记录最大数对和。
#
# 时间复杂度: O(n log n) — 排序的时间
# 空间复杂度: O(1) 或 O(n) — 取决于排序算法
#
# 关键点:
# - 排序后最小配最大是最优策略（贪心证明）
# - 返回的是所有数对和中的最大值
# - 数组长度为偶数
