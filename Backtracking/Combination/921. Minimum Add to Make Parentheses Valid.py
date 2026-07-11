"""
LeetCode #921 - Minimum Add to Make Parentheses Valid
中文题名：使括号有效的最少添加
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Given a string `S` of `'('` and `')'`
parentheses, we add the minimum number of parentheses ( `'('` or `')'`,
and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or

It can be written as `AB` (`A` concatenated with
`B`), where `A` and `B` are valid strings, or

It can be written as `(A)`, where `A` is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the
resulting string valid.

Example 1:

Input: "())"
Output: 1

Example 2:

Input: "((("
Output: 3

Example 3:

Input: "()"
Output: 0

Example 4:

Input: "()))(("
Output: 4

【中文翻译】

给定一个由 '(' 和 ')' 组成的括号字符串 S，我们需要添加最少数量的括号
（'(' 或 ')'，可以在任意位置），使得结果括号字符串有效。
形式化地，括号字符串有效当且仅当：
- 它是空字符串，或
- 它可以写成 AB（A 与 B 拼接），其中 A 和 B 都是有效字符串，或
- 它可以写成 (A)，其中 A 是有效字符串。
返回使字符串有效所需添加的最少括号数。

"""

from typing import List, Optional


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Track unbalanced '(' and ')'. For each char:
        - '(' : increment left_needed
        - ')' : if left_needed > 0, pair it (decrement), else increment right_needed
        Result = left_needed + right_needed
        """
        left_needed = 0   # unmatched '('
        right_needed = 0  # unmatched ')'

        for ch in s:
            if ch == '(':
                left_needed += 1
            else:  # ch == ')'
                if left_needed > 0:
                    left_needed -= 1
                else:
                    right_needed += 1

        return left_needed + right_needed



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 遍历字符串，维护两个计数器：
# - left_needed：当前未匹配的左括号数量（即需要多少右括号来匹配）
# - right_needed：遇到无法匹配的右括号时，需要添加的左括号数量
# 遇到 '(' 时 left_needed++，遇到 ')' 时如果有未匹配的左括号则配对(left_needed--)，
# 否则说明缺少左括号(right_needed++)。
# 最终答案 = left_needed + right_needed，即需要添加的括号总数。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 不需要实际构造字符串，只需计数
# - 类似经典的有效括号问题，但这里是计算最少添加量
# - 等价于：遍历后剩余的未匹配括号数就是答案
