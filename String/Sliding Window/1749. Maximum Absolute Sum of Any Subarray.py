"""
LeetCode #1749 - Maximum Absolute Sum of Any Subarray
中文题名：任意子数组和的绝对值的最大值
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

You are given an integer array `nums`. The absolute sum of a subarray `[numsl, numsl+1, ..., numsr-1, numsr]` is `abs(numsl + numsl+1 + ... + numsr-1 + numsr)`.

Return the maximum absolute sum of any (possibly empty) subarray of `nums`.

Note that `abs(x)` is defined as follows:

If `x` is a negative integer, then `abs(x) = -x`.

If `x` is a non-negative integer, then `abs(x) = x`.

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

Constraints:

`1 <= nums.length <= 105`

`-104 <= nums[i] <= 104`

【中文翻译】
给定一个整数数组 nums。子数组和定义为子数组所有元素的和。
返回任意子数组和的绝对值的最大值（即 abs(subarray_sum) 的最大值）。

示例 1：
输入: nums = [1,-3,2,3,-4]
输出: 5
解释: 子数组 [2,3] 的和为 5，abs(5)=5。

示例 2：
输入: nums = [2,-5,1,-4,3,-2]
输出: 8
解释: 子数组 [-5,1,-4] 的和为 -8，abs(-8)=8。
"""

from typing import List, Optional


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        cur_max = 0
        cur_min = 0

        for num in nums:
            cur_max = max(num, cur_max + num)
            cur_min = min(num, cur_min + num)
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)

        return max(max_sum, abs(min_sum))
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# Kadane 算法变体。同时维护以当前位置结尾的最大子数组和（cur_max）和最小子数组和（cur_min）。
# 绝对值最大的子数组和 = max(max_sum, abs(min_sum))。
# 因为 abs(subarray_sum) 最大值要么是最大正数和，要么是最小负数和的绝对值。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 同时跟踪最大正数和与最小负数和
# - Kadane 的标准转移：cur_max = max(num, cur_max+num)
