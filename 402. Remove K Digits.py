"""
LeetCode #402 - Remove K Digits
中文题名：移掉K位数字
https://leetcode.com/problems/remove-k-digits/

Given a non-negative integer num represented as a string, remove k digits from
the number so that the new number is the smallest possible.

Note:

The length of num is less than 10002 and will be >= k.

The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

【中文翻译】
给定一个以字符串表示的非负整数 num，移除 k 位数字，使得剩下的数字尽可能小。

注意：
    num 的长度小于 10002 且 >= k。
    给定的 num 不包含前导零。

示例 1：
    输入：num = "1432219", k = 3
    输出："1219"
    解释：移除数字 4, 3, 2 组成新数字 1219，这是可能的最小结果。

示例 2：
    输入：num = "10200", k = 1
    输出："200"
    解释：移除前导 1，数字为 200。注意输出不得包含前导零。

示例 3：
    输入：num = "10", k = 2
    输出："0"
    解释：移除所有数字后为空，视为 0。
"""

from typing import List, Optional


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If k remaining, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = "".join(stack).lstrip("0")

        return result if result else "0"


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用单调递增栈。从左到右遍历每位数字：
# 1. 当栈顶数字大于当前数字，且还能移除数字（k > 0）时，弹出栈顶（移除较大的高位数字）
# 2. 将当前数字压入栈中
#
# 遍历完成后，如果 k 仍大于 0（栈已是递增的），从尾部弹出剩余的 k 个数字。
# 最后去掉前导零。如果结果为空，返回 "0"。
#
# 核心贪心思想：为了让数字最小，高位的数字应该尽可能小。当我们遇到比栈顶更小的数字时，
# 移除栈顶能让高位变小，从而整体数字更小。
#
# 时间复杂度: O(N) — 每个数字最多入栈出栈各一次
# 空间复杂度: O(N) — 栈的空间
#
# 关键点:
# - 单调栈的思想：维护递增序列
# - 去掉前导零使用 lstrip("0")
# - 空字符串要返回 "0"
# - 贪心策略：遇到更小的数字就移除前面更大的数字
