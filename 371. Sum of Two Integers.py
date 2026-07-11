"""
LeetCode #371 - Sum of Two Integers
中文题名：两整数之和
https://leetcode.com/problems/sum-of-two-integers/

Calculate the sum of two integers a and b, but you are not allowed to
use the operator `+` and `-`.

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = -2, b = 3
Output: 1

【中文翻译】
不使用运算符 `+` 和 `-`，计算两整数 a、b 之和。

示例 1：

输入：a = 1, b = 2
输出：3

示例 2：

输入：a = -2, b = 3
输出：1
"""

from typing import List, Optional


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 位整数掩码，用于模拟 32 位有符号整数
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF  # 32 位有符号整数的最大值

        while b != 0:
            # 计算进位（仅保留 32 位）
            carry = (a & b) & MASK
            # 无进位加法（异或）
            a = (a ^ b) & MASK
            # 进位左移一位
            b = (carry << 1) & MASK

        # 处理负数：如果 a 超过 32 位有符号整数最大值，则转换为负数
        return a if a <= MAX_INT else ~(a ^ MASK)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用位运算模拟加法，核心思路是二进制加法器的原理：
# 1. 不考虑进位的加法：a XOR b 得到无进位和。
# 2. 进位：(a AND b) << 1 得到进位值。
# 3. 重复以上两步，直到进位为 0，此时 a 中存放的就是最终结果。
# Python 的整数是无限精度的，而题目要求模拟 32 位有符号整数加法。
# 因此需要使用掩码 0xFFFFFFFF 将结果限制在 32 位范围内。
# 对于 Python 来说，正数的 32 位表示与 int 一致，但负数的补码表示不同。
# 当结果超过 MAX_INT (0x7FFFFFFF) 时，说明在 32 位有符号整数中这是一个负数，
# 需要将其转换为 Python 的负数表示：~(a ^ MASK)。
# ~(a ^ MASK) 等价于 a | ~MASK，即对低 32 位取反后整体取反。
#
# 时间复杂度: O(1) - 最多迭代 32 次（每位最多进位一次）
# 空间复杂度: O(1) - 仅常数变量
#
# 关键点:
# - XOR 实现无进位加法，AND+左移实现进位计算
# - 循环直到进位为 0
# - Python 无限精度整数的特殊处理：需要用掩码模拟 32 位有符号整数
# - MASK = 0xFFFFFFFF 确保在位运算中只保留低 32 位
# - 负数转换：~(a ^ MASK) 将超过 MAX_INT 的 32 位正整数转为 Python 负数
