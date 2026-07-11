"""
LeetCode #1775 - Equal Sum Arrays With Minimum Number of Operations
中文题名：通过最少操作次数使数组和相等
https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

You are given two arrays of integers `nums1` and `nums2`, possibly of different lengths. The values in the arrays are between `1` and `6`, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between `1` and `6`, inclusive.

Return the minimum number of operations required to make the sum of values in `nums1` equal to the sum of values in `nums2`. Return `-1`​​​​​ if it is not possible to make the sum of the two arrays equal.

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].

Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.

Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].

Constraints:

`1 <= nums1.length, nums2.length <= 105`

`1 <= nums1[i], nums2[i] <= 6`

【中文翻译】
给定两个整数数组 nums1 和 nums2（元素值在 1 到 6 之间）。每次操作可以改变任意数组中任意一个元素为 1 到 6 之间的任意值。
求使两个数组的和相等所需的最少操作次数。如果不可能，返回 -1。

示例 1：
输入: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
输出: 3
解释: 将 nums1 中的 6→1（sum1 减少5），5→1（减少4），4→1（减少3），sum1 和 sum2 相等。
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0

        # 确保 nums1 的和较小（sum1 <= sum2）
        if sum1 > sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1

        diff = sum2 - sum1  # 需要增加 nums1 或减少 nums2 的总量

        # 对每个元素，计算它可以做出的贡献（改变量）
        contributions = []
        for num in nums1:
            # nums1 的元素可以增大到 6，贡献 = 6 - num
            contributions.append(6 - num)
        for num in nums2:
            # nums2 的元素可以减小到 1，贡献 = num - 1
            contributions.append(num - 1)

        # 从大到小排序贡献
        contributions.sort(reverse=True)

        ops = 0
        for contrib in contributions:
            diff -= contrib
            ops += 1
            if diff <= 0:
                return ops

        return -1
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略。设 sum1 < sum2，需要减少差值 diff = sum2 - sum1。
# nums1 的元素可以增大（贡献 = 6 - num），nums2 的元素可以减小（贡献 = num - 1）。
# 收集所有可能的贡献值，从大到小排序。
# 每次取最大贡献，从 diff 中减去，直到 diff <= 0。
# 如果所有贡献用完仍不能满足，返回 -1。
#
# 时间复杂度: O((N+M) log (N+M)) — 排序
# 空间复杂度: O(N+M) — 贡献数组
#
# 关键点:
# - 贪心优先选贡献最大的元素改变
# - 贡献值 = (6-num) for nums1, (num-1) for nums2
# - 思想：用最少的操作消除差值
