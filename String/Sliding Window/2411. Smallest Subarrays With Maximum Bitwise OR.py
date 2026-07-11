"""
LeetCode #2411 - Smallest Subarrays With Maximum Bitwise OR
按位或最大的最小子数组长度
https://leetcode.cn/problems/smallest-subarrays-with-maximum-bitwise-or/

给你一个长度为 `n` 下标从 0 开始的数组 `nums` ，数组中所有数字均为非负整数。对于 `0` 到 `n - 1` 之间的每一个下标 `i` ，你需要找出 `nums` 中一个 最小 非空子数组，它的起始位置为 `i` （包含这个位置），同时有 最大 的 按位或运算值 。
换言之，令 `B_ij` 表示子数组 `nums[i...j]` 的按位或运算的结果，你需要找到一个起始位置为 `i` 的最小子数组，这个子数组的按位或运算的结果等于 `max(B_ik)` ，其中 `i <= k <= n - 1` 。
一个数组的按位或运算值是这个数组里所有数字按位或运算的结果。
请你返回一个大小为 `n` 的整数数组 `answer`，其中 `answer[i]`是开始位置为 `i` ，按位或运算结果最大，且 最短 子数组的长度。
子数组 是数组里一段连续非空元素组成的序列。

示例 1：
输入：nums = [1,0,2,1,3] 输出：[3,3,2,2,1] 解释： 任何位置开始，最大按位或运算的结果都是 3 。 - 下标 0 处，能得到结果 3 的最短子数组是 [1,0,2] 。 - 下标 1 处，能得到结果 3 的最短子数组是 [0,2,1] 。 - 下标 2 处，能得到结果 3 的最短子数组是 [2,1] 。 - 下标 3 处，能得到结果 3 的最短子数组是 [1,3] 。 - 下标 4 处，能得到结果 3 的最短子数组是 [3] 。 所以我们返回 [3,3,2,2,1] 。
示例 2：
输入：nums = [1,2] 输出：[2,1] 解释： 下标 0 处，能得到最大按位或运算值的最短子数组长度为 2 。 下标 1 处，能得到最大按位或运算值的最短子数组长度为 1 。 所以我们返回 [2,1] 。

提示：
`n == nums.length`
`1 <= n <= 10^5`
`0 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        last = [0] * 30
        for i in range(n - 1, -1, -1):
            for b in range(30):
                if nums[i] & (1 << b):
                    last[b] = i
            max_last = i
            for b in range(30):
                if last[b] > max_last:
                    max_last = last[b]
            ans[i] = max(1, max_last - i + 1)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Binary Search, Sliding Window
#
# 解题思路:
# 从右向左遍历数组。维护每个bit位（共30位）最后出现的位置。
# 对于位置i，最大OR值需要覆盖nums[i]中所有设置位以及之后出现的所有不同bit位。
# 因此，从位置i开始的最小子数组需要延伸到所有bit位最后出现位置的最大值处。
# 答案长度为 max(1, max_last_pos - i + 1)。
#
# 时间复杂度: O(n * 30) = O(n)，n为数组长度。
# 空间复杂度: O(n)，用于存储答案数组。
#
# 关键点:
# - OR运算只会增加（或保持）bit位，不会减少，因此要最大化OR值就需覆盖尽可能多的不同bit位。
# - 从右向左遍历，维护每个bit位的最新出现位置。
# - 子数组长度由最远的bit位最后出现位置决定。
