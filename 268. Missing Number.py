"""
LeetCode #268 - Missing Number
中文题名：丢失的数字
https://leetcode.com/problems/missing-number/

Given an array containing *n* distinct numbers taken from `0, 1, 2, ..., n`,
find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:

Your algorithm should run in linear runtime complexity. Could you implement it using only
constant extra space complexity?

【中文翻译】
给定一个包含 *n* 个不同数字（取自 `0, 1, 2, ..., n`）的数组，找出数组中缺失的那个数。

示例 1：

输入：[3,0,1]
输出：2

示例 2：

输入：[9,6,4,2,3,5,7,0,1]
输出：8

注意：

你的算法应具有线性时间复杂度。你能否仅使用常数额外空间复杂度来实现？
"""

from typing import List, Optional


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # 数学方法：0 到 n 的和减去数组和
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路：
# 使用数学公式：0 到 n 的和 = n*(n+1)/2。
# 用期望和减去数组实际元素之和，差值即为缺失的数。
# 也可以用位运算（异或），将数组元素与 0..n 全部异或，
# 成对出现的数字会抵消，剩下的就是缺失数。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点：
# - 高斯求和公式: sum(0..n) = n*(n+1)/2
# - 异或法同样 O(n) O(1)，且不会溢出
# - 注意 n 是数组长度，0..n 共 n+1 个数
