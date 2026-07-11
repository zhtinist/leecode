"""
LeetCode #556 - Next Greater Element III
中文题名：下一个更大元素 III
https://leetcode.com/problems/next-greater-element-iii/

Given a positive 32-bit integer n, you need to find the
smallest 32-bit integer which has exactly the same digits existing in the
integer n and is greater in value than n. If no such positive 32-bit
integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21

Example 2:

Input: 21
Output: -1

【中文翻译】
给定一个 32 位正整数 n，你需要找到一个最小的 32 位整数，该整数与 n 拥有完全相同的数字，
且数值上大于 n。如果不存在这样的 32 位正整数，返回 -1。

示例 1：
    输入：12
    输出：21

示例 2：
    输入：21
    输出：-1
"""

from typing import List, Optional


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)

        # Step 1: 从右向左找到第一个下降的数字
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i < 0:
            return -1  # 已经是最大排列，无更大元素

        # Step 2: 从右向左找到第一个大于 digits[i] 的数字
        j = length - 1
        while j >= 0 and digits[j] <= digits[i]:
            j -= 1

        # Step 3: 交换
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: 反转 i 之后的部分
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int("".join(digits))
        return result if result <= 0x7FFFFFFF else -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题等价于"下一个排列"（LeetCode #31）。将整数转为数字列表后：
# 1. 从右向左找到第一个下降点（nums[i] < nums[i+1]）
# 2. 从右向左找到第一个大于 nums[i] 的数字，交换两者
# 3. 反转 i 之后的所有数字（使其变为升序，即最小排列）
# 4. 检查结果是否在 32 位有符号整数范围内（<= 2^31 - 1）
#
# 时间复杂度: O(D) — 其中 D 是数字位数（最多 10 位），实际可视为 O(1)
# 空间复杂度: O(D) — 存储数字列表
#
# 关键点:
# - 找到下降点是关键：保证交换后数字变大，且变化最小
# - 反转后缀使其最小化，保证结果是刚好大于原数的排列
# - 需要额外检查结果是否溢出 32 位整型
