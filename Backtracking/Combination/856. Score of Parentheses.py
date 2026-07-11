"""
LeetCode #856 - Score of Parentheses
中文题名：括号的分数
https://leetcode.com/problems/score-of-parentheses/

Given a balanced parentheses string `S`, compute the score of the string based on
the following rule:

`()` has score 1

`AB` has score `A + B`, where A and B are balanced parentheses
strings.

`(A)` has score `2 * A`, where A is a balanced parentheses string.

Example 1:

Input: "()"
Output: 1

Example 2:

Input: "(())"
Output: 2

Example 3:

Input: "()()"
Output: 2

Example 4:

Input: "(()(()))"
Output: 6

Note:

`S` is a balanced parentheses string, containing only
`(` and
`)`.

`2 <= S.length <= 50`

【中文翻译】
给定一个平衡括号字符串 S，根据以下规则计算字符串的分数：
- "()" 得 1 分。
- AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
- (A) 得 2 * A 分，其中 A 是平衡括号字符串。

"""

from typing import List, Optional


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # O(1) space solution using depth counting
        # Each "()" at depth d contributes 2^d to the total score
        score = 0
        depth = 0

        for i, ch in enumerate(s):
            if ch == '(':
                depth += 1
            else:
                depth -= 1
                # If this ')' closes a "()" pair (not a nested one)
                if s[i - 1] == '(':
                    score += 1 << depth  # 2^depth

        return score



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 方法一（使用栈）：遍历字符串，遇到 '(' 压入 0 作为占位符。遇到 ')' 时：
# 如果栈顶是 0，说明是 "()" 基本单元，弹出 0 并压入 1；
# 如果栈顶不是 0，说明是 "(A+B+...)"，将其中所有值弹出求和，乘以 2 后压入。
# 最后栈中所有值的和即为分数。
#
# 方法二（O(1) 空间，本实现）：统计深度法。
# 观察发现，每遇到一个 "()"（即 s[i-1]=='(' 且 s[i]==')'），
# 它对总分的贡献是 2^(当前深度)。深度是当前未闭合的 '(' 数量。
# 因为 "(())" 中内层 "()" 深度为 1，贡献 2^1 = 2。
# "(()(()))" 中第一个 "()" 深度 1（贡献 2），第二个 "()" 深度 2（贡献 4），总共 6。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - O(1) 空间解法：利用深度计数，每发现 "()" 就加 2^depth
# - 栈解法：遇到 '(' 压 0，遇到 ')' 若栈顶是 0（"()"）压 1；否则弹出求和乘 2 压回
# - 深度解法更简洁，但需要理解 "()" 的贡献与嵌套深度的指数关系
# - 使用位运算 1 << depth 快速计算 2^depth
