"""
LeetCode #2419 - Longest Subarray With Maximum Bitwise AND
按位与最大的最长子数组
https://leetcode.cn/problems/longest-subarray-with-maximum-bitwise-and/

给你一个长度为 `n` 的整数数组 `nums` 。
考虑 `nums` 中进行 按位与（bitwise AND）运算得到的值 最大 的 非空 子数组。
换句话说，令 `k` 是 `nums` 任意 子数组执行按位与运算所能得到的最大值。那么，只需要考虑那些执行一次按位与运算后等于 `k` 的子数组。
返回满足要求的 最长 子数组的长度。
数组的按位与就是对数组中的所有数字进行按位与运算。
子数组 是数组中的一个连续元素序列。

示例 1：
输入：nums = [1,2,3,3,2,2] 输出：2 解释： 子数组按位与运算的最大值是 3 。 能得到此结果的最长子数组是 [3,3]，所以返回 2 。
示例 2：
输入：nums = [1,2,3,4] 输出：1 解释： 子数组按位与运算的最大值是 4 。  能得到此结果的最长子数组是 [4]，所以返回 1 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_len = 0
        cur_len = 0
        for num in nums:
            if num == max_val:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Brainteaser, Array
#
# 解题思路:
# 关键洞察：按位与运算只会保持不变或变小，因此最大AND值就是数组中的最大值。
# 首先找出数组最大值max_val，然后找到由该最大值组成的最长连续子数组。
# 因为只有当子数组中所有元素都等于max_val时，AND结果才等于max_val。
#
# 时间复杂度: O(n)，只需两次遍历（找最大值+找最长连续段）。
# 空间复杂度: O(1)，只使用常数额外空间。
#
# 关键点:
# - 核心洞察：max AND = max(nums)，因为AND不增大数值。
# - 问题转化为找最长连续的max_val子数组。
# - 任何包含小于max_val的元素的子数组，AND结果一定小于max_val。
