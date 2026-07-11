"""
LeetCode #1802 - Maximum Value at a Given Index in a Bounded Array
中文题名：有界数组中指定下标处的最大值
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

You are given three positive integers `n`, `index` and `maxSum`. You want to construct an array `nums` (0-indexed) that satisfies the following conditions:

`nums.length == n`

`nums[i]` is a positive integer where `0 <= i < n`.

`abs(nums[i] - nums[i+1]) <= 1` where `0 <= i < n-1`.

The sum of all the elements of `nums` does not exceed `maxSum`.

`nums[index]` is maximized.

Return `nums[index]` of the constructed array.

Note that `abs(x)` equals `x` if `x >= 0`, and `-x` otherwise.

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: The arrays [1,1,2,1] and [1,2,2,1] satisfy all the conditions. There are no other valid arrays with a larger value at the given index.

Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3

Constraints:

`1 <= n <= maxSum <= 109`

`0 <= index < n`

【中文翻译】
给定三个整数 n、index 和 maxSum。构造一个长度为 n 的正整数数组 nums，
满足 nums[i] > 0 且相邻元素差的绝对值 <= 1，且 sum(nums) <= maxSum。
求 nums[index] 的最大可能值。

示例 1：
输入: n = 4, index = 2, maxSum = 6
输出: 2
解释: 数组 [1,2,1,2] 和 [1,2,2,1] 都是合法的，nums[2] 最大为 2。
"""

from typing import List, Optional


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def min_sum(val: int) -> int:
            # 计算以 index 为中心，峰值为 val 时的最小总和
            total = val
            # 左侧长度 = index
            left_len = index
            if val > left_len:
                # 左边可以形成 val-1, val-2, ..., val-left_len
                total += (val - 1 + val - left_len) * left_len // 2
            else:
                # 左边到1后需要全部填1
                total += val * (val - 1) // 2 + (left_len - (val - 1)) * 1

            # 右侧长度 = n - 1 - index
            right_len = n - 1 - index
            if val > right_len:
                total += (val - 1 + val - right_len) * right_len // 2
            else:
                total += val * (val - 1) // 2 + (right_len - (val - 1)) * 1

            return total

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if min_sum(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1

        return left
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 二分搜索 nums[index] 的值。对于给定的值 v，
# 构造最小和数组：index 位置为 v，向左依次递减至 1（不够则全 1），向右同理。
# 计算左右两侧的等差数列和 + 填充的 1。
# 如果最小和 <= maxSum，v 可行，尝试更大值。
#
# 时间复杂度: O(log maxSum)
# 空间复杂度: O(1)
#
# 关键点:
# - 要使 index 处值最大，其他位置应尽可能小（满足相邻差 <=1）
# - 数组形状是山峰形：从 index 向两侧递减
# - min_sum 函数需处理到 1 后填 1 的情况
