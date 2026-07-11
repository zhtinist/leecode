"""
LeetCode #2256 - Minimum Average Difference
最小平均差
https://leetcode.cn/problems/minimum-average-difference/

给你一个下标从 0 开始长度为 `n` 的整数数组 `nums` 。
下标 `i` 处的 平均差 指的是 `nums` 中 前 `i + 1` 个元素平均值和 后 `n - i - 1` 个元素平均值的 绝对差 。两个平均值都需要 向下取整 到最近的整数。
请你返回产生 最小平均差 的下标。如果有多个下标最小平均差相等，请你返回 最小 的一个下标。
注意：
两个数的 绝对差 是两者差的绝对值。
`n` 个元素的平均值是 `n` 个元素之 和 除以（整数除法） `n` 。
`0` 个元素的平均值视为 `0` 。

示例 1：
输入：nums = [2,5,3,9,5,3] 输出：3 解释： - 下标 0 处的平均差为：|2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3 。 - 下标 1 处的平均差为：|(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2 。 - 下标 2 处的平均差为：|(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2 。 - 下标 3 处的平均差为：|(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0 。  - 下标 4 处的平均差为：|(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1 。 - 下标 5 处的平均差为：|(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4 。 下标 3 处的平均差为最小平均差，所以返回 3 。
示例 2：
输入：nums = [0] 输出：0 解释： 唯一的下标是 0 ，所以我们返回 0 。 下标 0 处的平均差为：|0 / 1 - 0| = |0 - 0| = 0 。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        prefix = 0
        min_diff = float('inf')
        min_idx = 0

        for i in range(n):
            prefix += nums[i]
            left_avg = prefix // (i + 1)

            if i < n - 1:
                right_avg = (total - prefix) // (n - i - 1)
            else:
                right_avg = 0  # last element: right side has 0 elements

            diff = abs(left_avg - right_avg)

            if diff < min_diff:
                min_diff = diff
                min_idx = i

        return min_idx


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum
#
# 解题思路:
# 使用前缀和技巧一次遍历完成。
# 首先计算数组总和 total。
# 然后遍历每个下标 i，维护前缀和 prefix：
#   - 左半部分平均值 = prefix // (i + 1)
#   - 右半部分平均值 = (total - prefix) // (n - i - 1)，若 i == n-1 则为 0
#   - 计算绝对差，记录最小差及其下标
#
# 因为要求最小下标，只有当 diff < min_diff 时才更新（不用 <=）。
#
# 时间复杂度: O(n) — 一次计算总和 + 一次遍历
# 空间复杂度: O(1) — 只使用常数额外空间
#
# 关键点:
# - 前缀和避免重复计算子数组和
# - 右半部分元素个数为 0 时平均值为 0（最后一个下标处）
# - 整数除法自动向下取整（Python // 对正数即 floor）
# - 只在严格小于时更新，保证返回最小下标
