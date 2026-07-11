"""
LeetCode #3634 - Minimum Removals to Balance Array
使数组平衡的最少移除数目
https://leetcode.cn/problems/minimum-removals-to-balance-array/

给你一个整数数组 `nums` 和一个整数 `k`。
如果一个数组的 最大 元素的值 至多 是其 最小 元素的 `k` 倍，则该数组被称为是 平衡 的。
你可以从 `nums` 中移除 任意 数量的元素，但不能使其变为 空 数组。
返回为了使剩余数组平衡，需要移除的元素的 最小 数量。
注意：大小为 1 的数组被认为是平衡的，因为其最大值和最小值相等，且条件总是成立。

示例 1:

输入：nums = [2,1,5], k = 2
输出：1
解释：
移除 `nums[2] = 5` 得到 `nums = [2, 1]`。
现在 `max = 2`, `min = 1`，且 `max <= min * k`，因为 `2 <= 1 * 2`。因此，答案是 1。
示例 2:

输入：nums = [1,6,2,9], k = 3
输出：2
解释：
移除 `nums[0] = 1` 和 `nums[3] = 9` 得到 `nums = [6, 2]`。
现在 `max = 6`, `min = 2`，且 `max <= min * k`，因为 `6 <= 2 * 3`。因此，答案是 2。
示例 3:

输入：nums = [4,6], k = 2
输出：0
解释：
由于 `nums` 已经平衡，因为 `6 <= 4 * 2`，所以不需要移除任何元素。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`1 <= k <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minRemovals(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_len = 0
        j = 0
        for i in range(n):
            # 扩展右边界直到 nums[j] > nums[i] * k
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            max_len = max(max_len, j - i)
        return n - max_len










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Sorting, Sliding Window
#
# 解题思路:
# 排序后问题转化为：在排序数组中找最长的子数组，使得子数组的最大值 ≤ 最小值 * k。
# 使用双指针/滑动窗口：对于每个左端点 i，右指针 j 向右扩展到第一个不满足
# nums[j] <= nums[i] * k 的位置。窗口长度 j-i 就是以 i 为最小值的最大平衡子数组长度。
# 记录所有窗口的最大长度 max_len，答案为 n - max_len（需要移除的元素数）。
#
# 时间复杂度: O(n log n) — 排序开销
# 空间复杂度: O(1) — 仅使用常数额外空间
#
# 关键点:
# - 排序后滑动窗口找到最大平衡子数组
# - 双指针确保整体 O(n) 的窗口移动（每个元素最多被左右指针各访问一次）
