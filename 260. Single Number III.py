"""
LeetCode #260 - Single Number III
https://leetcode.com/problems/single-number-iii/

Given an array of numbers `nums`, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that appear only
once.

Example:

Input:  `[1,2,1,3,2,5]`
Output: `[3,5]`

Note:

The order of the result is not important. So in the above example, `[5, 3]`
is also correct.

Your algorithm should run in linear runtime complexity. Could you implement it using
only constant space complexity?
"""

from typing import List, Optional


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 第一步：所有数异或，得到两个不同数的异或结果
        xor_all = 0
        for num in nums:
            xor_all ^= num

        # 第二步：找到 xor_all 中最低位的 1（用于分组）
        # diff_bit = xor_all & (-xor_all)  # 取最低位 1
        diff_bit = xor_all & -xor_all

        # 第三步：根据该位是否为 1 将数组分为两组，分别异或
        a = b = 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路：
# 位运算 O(n) 时间 O(1) 空间。分为三步：
# 1. 所有数异或，结果 xor_all = a ^ b（两个只出现一次的数异或）。
# 2. 取 xor_all 中任意一个为 1 的位（如最低位 1 = xor_all & -xor_all）。
#    因为 a 和 b 不同，至少某一位不同。
# 3. 根据该位是 0 还是 1，将数组分成两组，每组分别异或，
#    每组中的成对元素会被抵消，剩下的就是 a 和 b。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点：
# - xor_all = a ^ b
# - 取最低位 1 进行分组：xor_all & -xor_all
# - 分组后每一组都变成 Single Number I 的问题
