"""
LeetCode #678 - Valid Parenthesis String
中文题名：有效的括号字符串
https://leetcode.com/problems/valid-parenthesis-string/

Given a string containing only three types of characters: '(', ')' and '*', write a function
to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.

Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.

Left parenthesis `'('` must go before the corresponding right parenthesis
`')'`.

`'*'` could be treated as a single right parenthesis `')'` or a
single left parenthesis `'('` or an empty string.

An empty string is also valid.

Example 1:

Input: "()"
Output: True

Example 2:

Input: "(*)"
Output: True

Example 3:

Input: "(*))"
Output: True

Note:

The string size will be in the range [1, 100].

【中文翻译】
给定一个只包含三种字符的字符串：'('、')' 和 '*'，写一个函数来检验这个字符串是否为有效字符串。有效字符串的定义如下：

任何左括号 `'('` 必须有相应的右括号 `')'`。

任何右括号 `')'` 必须有相应的左括号 `'('`。

左括号 `'('` 必须在对应的右括号 `')'` 之前。

`'*'` 可以被视为单个右括号 `')'`、单个左括号 `'('` 或空字符串。

空字符串也是有效的。

示例 1：

输入: "()"
输出: True

示例 2：

输入: "(*)"
输出: True

示例 3：

输入: "(*))"
输出: True

注意：

字符串大小将在 [1, 100] 范围内。
"""

from typing import List, Optional


class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo = max(lo - 1, 0)
                hi -= 1
            else:  # '*'
                lo = max(lo - 1, 0)
                hi += 1
            if hi < 0:
                return False
        return lo == 0









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用贪心法，维护未匹配左括号的可能数量范围 [lo, hi]。
# - lo: 最少有多少个未匹配的左括号（将尽量多的 '*' 视为 ')' 或空）
# - hi: 最多有多少个未匹配的左括号（将所有 '*' 视为 '('）
# 遍历每个字符：
# - 遇到 '('：lo 和 hi 各加 1。
# - 遇到 ')'：lo 减 1（但不低于 0），hi 减 1。如果 hi < 0 说明右括号过多，返回 False。
# - 遇到 '*'：lo 减 1（视为 ')' 或空，但不低于 0），hi 加 1（视为 '('）。
# 最终 lo == 0 表示可以将所有左括号匹配完毕（通过将部分 '*' 视为 ')'）。
#
# 时间复杂度: O(n) - 一次遍历
# 空间复杂度: O(1) - 仅使用两个变量
#
# 关键点:
# - 维护可能范围而非具体值
# - lo 不能低于 0（不能有负的左括号数）
# - hi < 0 时必然无效
# - 最终 lo == 0 才有效
