"""
LeetCode #713 - Subarray Product Less Than K
中文题名：乘积小于K的子数组
https://leetcode.com/problems/subarray-product-less-than-k/

Your are given an array of positive integers `nums`.

Count and print the number of (contiguous) subarrays where the product of all the elements in
the subarray is less than `k`.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:

`0 < nums.length <= 50000`.

`0 < nums[i] < 1000`.

`0 <= k < 10^6`.

【中文翻译】
给定一个正整数数组 `nums`。

计数并输出（连续）子数组的数量，其中子数组中所有元素的乘积小于 `k`。

示例 1：

输入: nums = [10, 5, 2, 6], k = 100
输出: 8
解释: 乘积小于 100 的 8 个子数组为：[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]。
注意 [10, 5, 2] 不被包含，因为其乘积 100 不小于 k。

注意：

`0 < nums.length <= 50000`。

`0 < nums[i] < 1000`。

`0 <= k < 10^6`。
"""

from typing import List, Optional


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        ans = left = 0
        for right, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用滑动窗口（双指针）技术。
# 维护窗口 [left, right]，窗口内乘积 prod < k。
# 对于每个 right，扩展右侧边界，将 nums[right] 乘入 prod。
# 如果 prod >= k，收缩左侧边界 left，直到 prod < k（或 left > right）。
# 此时以 right 结尾的、乘积小于 k 的子数组数量 = right - left + 1
# （所有 [left, right], [left+1, right], ..., [right, right] 都满足条件）。
#
# 特殊情况：k <= 1 时，没有乘积可能小于 1（因为所有数 >= 1），直接返回 0。
#
# 时间复杂度: O(n) - 每个元素最多被 left 和 right 各访问一次
# 空间复杂度: O(1) - 仅使用常数变量
#
# 关键点:
# - 滑动窗口维护乘积满足条件的最大窗口
# - 以 right 结尾的满足条件的子数组数量 = right - left + 1
# - k <= 1 的边界情况
