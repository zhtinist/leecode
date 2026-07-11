"""
LeetCode #1695 - Maximum Erasure Value
中文题名：删除子数组的最大得分
https://leetcode.com/problems/maximum-erasure-value/

You are given an array of positive integers `nums` and want to erase a
subarray containing unique elements. The score
you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly
one subarray.

An array `b` is called to be a subarray of `a` if it forms a
contiguous subsequence of `a`, that is, if it is equal to `a[l],a[l+1],...,a[r]`
for some `(l,r)`.

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:

`1 <= nums.length <= 105`

`1 <= nums[i] <= 104`

【中文翻译】
给定一个正整数数组 `nums`，你希望删除一个包含唯一元素的子数组。
删除子数组的得分等于其元素之和。

返回恰好删除一个子数组可以得到的最大得分。

如果数组 `b` 是 `a` 的连续子序列，即等于 `a[l],a[l+1],...,a[r]`（对于某些 `(l,r)`），
则称 `b` 是 `a` 的子数组。

示例 1：

输入: nums = [4,2,4,5,6]
输出: 17
解释: 最优子数组是 [2,4,5,6]

示例 2：

输入: nums = [5,2,1,2,5,2,1,2,5]
输出: 8
解释: 最优子数组是 [5,2,1] 或 [1,2,5]

约束条件：

`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^4`
"""

from typing import List, Optional


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        滑动窗口 + 哈希集合：维护一个元素唯一的窗口，
        右指针扩展窗口，当遇到重复元素时，左指针收缩直到窗口内无重复。
        同时维护窗口内元素之和，更新最大得分。
        """
        seen = set()
        left = 0
        cur_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            # 当右指针元素已在窗口内，收缩左边界
            while nums[right] in seen:
                seen.remove(nums[left])
                cur_sum -= nums[left]
                left += 1
            # 加入右指针元素
            seen.add(nums[right])
            cur_sum += nums[right]
            max_sum = max(max_sum, cur_sum)

        return max_sum










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 滑动窗口经典应用。要求找到元素唯一的子数组的最大和。
# 使用两个指针 left 和 right 维护一个窗口，窗口内的元素互不相同。
# 右指针 right 逐个扫描数组：
# - 如果 nums[right] 不在窗口中，加入窗口，更新窗口和与最大和。
# - 如果 nums[right] 已在窗口中，不断移动左指针 left 并移除 nums[left]，
#   直到 nums[right] 可以加入窗口。
# 同时维护 cur_sum 为当前窗口的和，避免每次重新计算。
#
# 时间复杂度: O(n)，每个元素最多被加入和移除集合各一次
# 空间复杂度: O(n)，哈希集合最坏存储所有元素
#
# 关键点:
# - 滑动窗口 + 哈希集合维护唯一性
# - 维护 running sum 避免重复求和
# - 每个元素被处理 O(1) 次，总体线性时间
