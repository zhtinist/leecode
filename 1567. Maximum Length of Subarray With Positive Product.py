"""
LeetCode #1567 - Maximum Length of Subarray With Positive Product
中文题名：乘积为正数的最长子数组长度
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/


Given an array of integers `nums, find` the maximum length of a
subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of
that array.

Return the maximum length of a subarray with positive product.

Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].

Example 4:

Input: nums = [-1,2]
Output: 1

Example 5:

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4

Constraints:

`1 <= nums.length <= 10^5`

`-10^9 <= nums[i] <= 10^9`

【中文翻译】
给定一个整数数组 nums，返回乘积为正数的最长连续子数组的长度。

示例 1：
输入：nums = [1,-2,-3,4]
输出：4
解释：整个数组乘积为正。

示例 2：
输入：nums = [0,1,-2,-3,-4]
输出：3
解释：子数组 [1,-2,-3] 乘积为正。

示例 3：
输入：nums = [-1,-2,-3,0,1]
输出：2
"""

from typing import List, Optional


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos_len = 0  # length of subarray ending here with positive product
        neg_len = 0  # length of subarray ending here with negative product
        result = 0
        for num in nums:
            if num == 0:
                pos_len = 0
                neg_len = 0
            elif num > 0:
                pos_len += 1
                neg_len = neg_len + 1 if neg_len > 0 else 0
            else:  # num < 0
                new_pos = neg_len + 1 if neg_len > 0 else 0
                new_neg = pos_len + 1
                pos_len, neg_len = new_pos, new_neg
            result = max(result, pos_len)
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。维护两个变量：pos_len（以当前位置结尾乘积为正的子数组最大长度）和
# neg_len（以当前位置结尾乘积为负的子数组最大长度）。
# 遇到 0 时重置。遇到正数时正数长度 +1，负数长度如果 >0 则 +1。
# 遇到负数时，正负长度互换：新正数长度 = 旧负数长度 + 1（如果旧负数长度 > 0），
# 新负数长度 = 旧正数长度 + 1。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 正*正=正，负*负=正，正*负=负
# - 遇到 0 重置所有状态
# - 仅需维护两个状态变量












