"""
LeetCode #3002 - Maximum Size of a Set After Removals
移除后集合的最多元素数
https://leetcode.cn/problems/maximum-size-of-a-set-after-removals/

给你两个下标从 `0` 开始的整数数组 `nums1` 和 `nums2` ，它们的长度都是偶数` n` 。
你必须从 `nums1` 中移除 `n / 2` 个元素，同时从 `nums2` 中也移除 `n / 2` 个元素。移除之后，你将 `nums1` 和 `nums2` 中剩下的元素插入到集合 `s` 中。
返回集合 `s`可能的 最多 包含多少元素。

示例 1：
输入：nums1 = [1,2,1,2], nums2 = [1,1,1,1] 输出：2 解释：从 nums1 和 nums2 中移除两个 1 。移除后，数组变为 nums1 = [2,2] 和 nums2 = [1,1] 。因此，s = {1,2} 。 可以证明，在移除之后，集合 s 最多可以包含 2 个元素。
示例 2：
输入：nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3] 输出：5 解释：从 nums1 中移除 2、3 和 6 ，同时从 nums2 中移除两个 3 和一个 2 。移除后，数组变为 nums1 = [1,4,5] 和 nums2 = [2,3,2] 。因此，s = {1,2,3,4,5} 。 可以证明，在移除之后，集合 s 最多可以包含 5 个元素。
示例 3：
输入：nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6] 输出：6 解释：从 nums1 中移除 1、2 和 3 ，同时从 nums2 中移除 4、5 和 6 。移除后，数组变为 nums1 = [1,2,3] 和 nums2 = [4,5,6] 。因此，s = {1,2,3,4,5,6} 。 可以证明，在移除之后，集合 s 最多可以包含 6 个元素。

提示：
`n == nums1.length == nums2.length`
`1 <= n <= 2 * 10^4`
`n`是偶数。
`1 <= nums1[i], nums2[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Compute sets and their intersections. Only1 elements can only come from
        nums1 slots, only2 only from nums2 slots. Common elements can fill either.
        Prioritize only1/only2 for their respective arrays' n/2 slots.
        """
        n = len(nums1)
        half = n // 2

        set1 = set(nums1)
        set2 = set(nums2)
        common = set1 & set2
        only1 = set1 - common
        only2 = set2 - common

        # Elements only in nums1: limited by half
        take_only1 = min(len(only1), half)
        # Elements only in nums2: limited by half
        take_only2 = min(len(only2), half)

        # Remaining slots in each array after taking exclusive elements
        rem1 = half - take_only1
        rem2 = half - take_only2

        # Common elements can fill remaining slots from either side
        take_common = min(len(common), rem1 + rem2)

        return take_only1 + take_only2 + take_common



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table
#
# 解题思路:
# 将两个数组的元素分为三类：仅在 nums1 中的、仅在 nums2 中的、两者共有的。
# nums1 独有元素只能占用 nums1 的 n/2 个保留名额，num2 独有同理，优先分配。
# 剩余名额用于共有元素，共有元素可以从任一侧保留，因此可用名额为两部分剩余之和。
# 最终答案 = 各自独有保留数 + 共有元素保留数。
#
# 时间复杂度: O(n)，构建集合和交集
# 空间复杂度: O(n)，存储两个集合
#
# 关键点:
# - 集合分类是关键：独有元素只能从对应数组保留，共有元素灵活
# - 优先保留独有元素（因为共有元素有更多来源选择）
# - 保留名额即 n/2 个"槽位"，每个不同元素至少占一个槽位
