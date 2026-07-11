"""
LeetCode #1249 - Minimum Remove to Make Valid Parentheses
中文题名：移除无效的括号
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of `'('` , `')'` and
lowercase English characters.

Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in
any positions ) so that the resulting parentheses string is valid and return
any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or

It can be written as `AB` (`A` concatenated with `B`),
where `A` and `B` are valid strings, or

It can be written as `(A)`, where `A` is a valid
string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

Constraints:

`1 <= s.length <= 10^5`

`s[i]` is one of  `'('` , `')'`
and lowercase English letters`.`

【中文翻译】
给你一个由 `'('`、`')'` 和小写英文字母组成的字符串 `s`。

你需要从字符串中删除最少数目的括号（`'('` 或 `')'`，可以在任意位置），使得剩下的「括号字符串」有效。请返回任意一个有效字符串。

「括号字符串」有效的形式化定义如下：

- 它是空字符串，或只包含小写字母，或
- 它可以写作 `AB`（`A` 与 `B` 连接），其中 `A` 和 `B` 都是有效字符串，或
- 它可以写作 `(A)`，其中 `A` 是一个有效字符串。

示例 1：

输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" 和 "lee(t(c)ode)" 也是可接受的答案。

示例 2：

输入：s = "a)b(c)d"
输出："ab(c)d"

示例 3：

输入：s = "))(("
输出：""
解释：空字符串也是有效的。

示例 4：

输入：s = "(a(b(c)d)"
输出："a(b(c)d)"

约束条件：

`1 <= s.length <= 10^5`

`s[i]` 是 `'('`、`')'` 或小写英文字母之一。
"""

from typing import List, Optional


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: mark extra ')' to remove
        chars = list(s)
        stack = []

        for i, ch in enumerate(chars):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''  # Mark extra ')' for removal

        # Second pass: mark extra '(' to remove (remaining in stack)
        for i in stack:
            chars[i] = ''

        return ''.join(chars)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈（stack）来标记需要删除的括号的索引。
# 1. 第一遍扫描：从左到右遍历字符串。
#    - 遇到 '(' ，将索引压入栈。
#    - 遇到 ')' ：
#      * 如果栈非空，弹出栈顶（匹配了一个 '(' ）。
#      * 如果栈为空，说明这个 ')' 是多余的，标记删除（设为 ''）。
# 2. 第二遍处理：栈中剩余的索引都是无法匹配的多余 '('，将它们标记删除。
# 3. 将字符数组拼接成字符串返回。
# 这种方法的本质是：保留能配对的括号，删除不配对的。栈记录了尚未配对的 '(' 的位置。
#
# 时间复杂度: O(N)，一次遍历 + 一次栈遍历
# 空间复杂度: O(N)，字符数组和栈的空间
#
# 关键点:
# - 将字符串转为列表（mutable），便于原地标记删除
# -栈存索引而非字符，方便定位和删除
# - 多余的 ')' 在第一次遍历时就能识别（栈为空时遇到的 ')'）
# - 多余的 '(' 在遍历结束后留在栈中
# - 也可以用 balance 计数（先正向去多余的 ')'，再反向去多余的 '('）
