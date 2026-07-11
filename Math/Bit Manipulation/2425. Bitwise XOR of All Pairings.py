"""
LeetCode #2425 - Bitwise XOR of All Pairings
所有数对的异或和
https://leetcode.cn/problems/bitwise-xor-of-all-pairings/

给你两个下标从 0 开始的数组 `nums1` 和 `nums2` ，两个数组都只包含非负整数。请你求出另外一个数组 `nums3` ，包含 `nums1` 和 `nums2` 中 所有数对 的异或和（`nums1` 中每个整数都跟 `nums2` 中每个整数 恰好 匹配一次）。
请你返回 `nums3` 中所有整数的 异或和 。

示例 1：
输入：nums1 = [2,1,3], nums2 = [10,2,5,0] 输出：13 解释： 一个可能的 nums3 数组是 [8,0,7,2,11,3,4,1,9,1,6,3] 。 所有这些数字的异或和是 13 ，所以我们返回 13 。
示例 2：
输入：nums1 = [1,2], nums2 = [3,4] 输出：0 解释： 所有数对异或和的结果分别为 nums1[0] ^ nums2[0] ，nums1[0] ^ nums2[1] ，nums1[1] ^ nums2[0] 和 nums1[1] ^ nums2[1] 。 所以，一个可能的 nums3 数组是 [2,5,1,6] 。 2 ^ 5 ^ 1 ^ 6 = 0 ，所以我们返回 0 。

提示：
`1 <= nums1.length, nums2.length <= 10^5`
`0 <= nums1[i], nums2[j] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        result = 0

        # Each element in nums1 appears n2 times in the pairwise XORs.
        # If n2 is odd, those XOR to the element itself.
        if n2 % 2 == 1:
            for x in nums1:
                result ^= x

        # Each element in nums2 appears n1 times.
        # If n1 is odd, those XOR to the element itself.
        if n1 % 2 == 1:
            for x in nums2:
                result ^= x

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Brainteaser, Array
#
# 解题思路:
# 所有数对的异或和等价于：
#   XOR over all (nums1[i] ^ nums2[j])
# 由于 XOR 满足结合律和交换律，每个 nums1[i] 会出现 len(nums2) 次，
# 每个 nums2[j] 会出现 len(nums1) 次。
# 当某个元素出现偶数次时，XOR 结果为 0；奇数次时则是元素本身。
# 因此只需：
# - 如果 len(nums2) 为奇数，将 nums1 的所有元素异或到结果
# - 如果 len(nums1) 为奇数，将 nums2 的所有元素异或到结果
# 两者的 XOR 即为最终答案，无需生成任何中间数组。
#
# 时间复杂度: O(n + m) — 遍历两个数组
# 空间复杂度: O(1) — 只使用常量额外空间
#
# 关键点:
# - XOR 的交换律和结合律使得可以按元素计数而不是逐对计算
# - 偶数次 XOR 抵消（x ^ x = 0），只需关注奇数次出现的元素
# - 不需要实际生成 nums3 数组，避免了 O(n*m) 的暴力枚举
