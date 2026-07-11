"""
LeetCode #209 - Minimum Size Subarray Sum
中文题名：长度最小的子数组
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer
s, find the minimal length of a contiguous subarray of which the sum
>= s. If there isn't one, return 0 instead.

Example:

Input: `s = 7, nums = [2,3,1,2,4,3]`
Output: 2
Explanation: the subarray `[4,3]` has the minimal length under the problem constraint.

Follow up:

【中文翻译】
给定一个含有 n 个正整数的数组和一个正整数 s，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：`s = 7, nums = [2,3,1,2,4,3]`
输出：2
解释：子数组 `[4,3]` 是该条件下的长度最小的子数组。

进阶：
"""

from typing import List, Optional


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float("inf")

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink window from left while sum >= target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 滑动窗口（双指针）。维护一个可变长度的窗口 [left, right]：
# 1. right 指针不断右移，累加 current_sum
# 2. 当 current_sum >= target 时，尝试收缩 left 指针：
#    - 更新 min_len = min(min_len, right - left + 1)
#    - current_sum 减去 nums[left]
#    - left 右移
# 3. 重复直到 right 遍历完数组
#
# 因为所有数字都是正整数，所以扩大窗口 sum 递增，缩小窗口 sum 递减，
# 滑动窗口方法是正确的。
#
# 时间复杂度: O(N) — 每个元素最多被 left 和 right 各访问一次
# 空间复杂度: O(1) — 只使用常数变量
#
# 关键点:
# - 滑动窗口适用于"正数数组 + 连续子数组"问题
# - 两个 while 循环看似 O(N^2)，但每个元素进一次出一共 O(N)
# - 也可用前缀和 + 二分查找，时间复杂度 O(N log N)
