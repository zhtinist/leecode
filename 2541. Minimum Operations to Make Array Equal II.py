"""
LeetCode #2541 - Minimum Operations to Make Array Equal II
使数组中所有元素相等的最小操作数 II
https://leetcode.cn/problems/minimum-operations-to-make-array-equal-ii/

给你两个整数数组 `nums1` 和 `nums2` ，两个数组长度都是 `n` ，再给你一个整数 `k` 。你可以对数组 `nums1` 进行以下操作：
选择两个下标 `i` 和 `j` ，将 `nums1[i]` 增加 `k` ，将 `nums1[j]` 减少 `k` 。换言之，`nums1[i] = nums1[i] + k` 且 `nums1[j] = nums1[j] - k` 。
如果对于所有满足 `0 <= i < n` 都有 `num1[i] == nums2[i]` ，那么我们称 `nums1` 等于 `nums2` 。
请你返回使 `nums1` 等于 `nums2` 的 最少 操作数。如果没办法让它们相等，请你返回 `-1` 。

示例 1：
输入：nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3 输出：2 解释：我们可以通过 2 个操作将 nums1 变成 nums2 。 第 1 个操作：i = 2 ，j = 0 。操作后得到 nums1 = [1,3,4,4] 。 第 2 个操作：i = 2 ，j = 3 。操作后得到 nums1 = [1,3,7,1] 。 无法用更少操作使两个数组相等。
示例 2：
输入：nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1 输出：-1 解释：无法使两个数组相等。

提示：
`n == nums1.length == nums2.length`
`2 <= n <= 10^5`
`0 <= nums1[i], nums2[j] <= 10^9`
`0 <= k <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1

        pos_sum = 0
        neg_sum = 0
        for a, b in zip(nums1, nums2):
            diff = b - a
            if diff % k != 0:
                return -1
            if diff > 0:
                pos_sum += diff
            else:
                neg_sum += -diff

        if pos_sum != neg_sum:
            return -1
        return pos_sum // k



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Math
#
# 解题思路:
# 计算每个位置需要的差值diff=b-a。每次操作将k从一处移到另一处，总和不改变。
# 若总正差值和总负差值绝对值不相等则不可能。每个diff必须是k的倍数，否则无法通过操作达成。
# 操作数等于正差值和除以k（每个操作消除k的正差和一个k的负差）。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 操作保持数组总和不变，所以总差值必须为0
# - k=0是特殊情况：如果两数组已相等则0次，否则不可能
# - 每个diff必须能被k整除，操作数=正差值总和/k
