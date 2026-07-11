"""
LeetCode #3097 - Shortest Subarray With OR at Least K II
或值至少为 K 的最短子数组 II
https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/

给你一个 非负 整数数组 `nums` 和一个整数 `k` 。
如果一个数组中所有元素的按位或运算 `OR` 的值 至少 为 `k` ，那么我们称这个数组是 特别的 。
请你返回 `nums` 中 最短特别非空 子数组的长度，如果特别子数组不存在，那么返回 `-1` 。

示例 1：

输入：nums = [1,2,3], k = 2
输出：1
解释：
子数组 `[3]` 的按位 `OR` 值为 `3` ，所以我们返回 `1` 。
示例 2：

输入：nums = [2,1,8], k = 10
输出：3
解释：
子数组 `[2,1,8]` 的按位 `OR` 值为 `11` ，所以我们返回 `3` 。
示例 3：

输入：nums = [1,2], k = 0
输出：1
解释：
子数组 `[1]` 的按位 `OR` 值为 `1` ，所以我们返回 `1` 。

提示：
`1 <= nums.length <= 2 * 10^5`
`0 <= nums[i] <= 10^9`
`0 <= k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1  # 任何元素OR值都>=0
        n = len(nums)
        bits = [0] * 32  # 每个bit在当前窗口中被设置的次数
        cur_or = 0
        ans = n + 1

        def add_val(x: int):
            nonlocal cur_or
            cur_or |= x
            for b in range(32):
                if x & (1 << b):
                    bits[b] += 1

        def remove_val(x: int):
            nonlocal cur_or
            for b in range(32):
                if x & (1 << b):
                    bits[b] -= 1
                    if bits[b] == 0:
                        cur_or &= ~(1 << b)

        left = 0
        for right in range(n):
            add_val(nums[right])
            while left <= right and cur_or >= k:
                ans = min(ans, right - left + 1)
                remove_val(nums[left])
                left += 1

        return ans if ans <= n else -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Sliding Window
#
# 解题思路:
# 使用滑动窗口+位计数技术。OR运算不可逆（无法直接移除左侧元素的影响），
# 因此维护32个bit的计数器数组。添加元素时对每个bit增计数，
# 移除元素时减计数，当某个bit计数归零时从当前OR值中清除该bit。
# 滑动窗口右扩，当cur_or>=k时收缩左边界更新最短长度。
#
# 时间复杂度: O(32*n) = O(n)
# 空间复杂度: O(32) = O(1)
#
# 关键点:
# - OR操作不可逆，不能像求和那样直接减去
# - 用bit计数数组跟踪每个bit被多少个元素覆盖
# - 当某个bit计数归零时才从cur_or中移除该bit
