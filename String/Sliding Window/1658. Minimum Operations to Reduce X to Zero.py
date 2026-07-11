"""
LeetCode #1658 - Minimum Operations to Reduce X to Zero
中文题名：将 x 减到 0 的最小操作数
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

You are given an integer array `nums` and an integer `x`. In
one operation, you can either remove the leftmost or the rightmost element from the
array `nums` and subtract its value from `x`. Note that this
modifies the array for future operations.

Return the minimum number of operations to reduce
`x` to exactly `0` if it's
possible, otherwise, return `-1`.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

Constraints:

`1 <= nums.length <= 105`

`1 <= nums[i] <= 104`

`1 <= x <= 109`

【中文翻译】
给定整数数组 nums 和整数 x。每次操作可以从数组的最左端或最右端移除一个元素，并从 x 中减去该元素的值。
求将 x 恰好减为 0 所需的最少操作次数。如果不可能，返回 -1。

示例 1：
输入: nums = [1,1,4,2,3], x = 5
输出: 2
解释: 移除最右边的3（x=2），再移除最右边的2（x=0），共2步。

示例 2：
输入: nums = [5,6,7,8,9], x = 4
输出: -1
解释: 无法将 x 减为 0。
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        n = len(nums)
        left = 0
        cur_sum = 0
        max_len = -1

        for right in range(n):
            cur_sum += nums[right]
            while cur_sum > target and left <= right:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 问题转化为：从数组两端移除元素使和为 x，等价于找一个最长的子数组使和为 total - x。
# 因为移除的总元素数 = n - 中间保留的子数组长度。
# 使用滑动窗口找到和等于 target = total - x 的最长子数组。
# 答案 = n - max_len。若找不到这样的子数组返回 -1。
#
# 时间复杂度: O(N) — 滑动窗口每个元素最多访问两次
# 空间复杂度: O(1)
#
# 关键点:
# - 将从两端移除转化为保留一个连续子数组的关键思维
# - 滑动窗口求特定和的最长子数组
