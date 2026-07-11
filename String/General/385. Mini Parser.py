"""
LeetCode #385 - Mini Parser
中文题名：迷你语法分析器
https://leetcode.com/problems/mini-parser/

Given a nested list of integers represented as a string, implement a parser to deserialize
it.

Each element is either an integer, or a list -- whose elements may also be integers or other
lists.

Note:
You may assume that the string is well-formed:

String is non-empty.

String does not contain white spaces.

String contains only digits `0-9`, `[`, `-`
`,`, `]`.

Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.

Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
i.  An integer containing value 456.
ii. A nested list with one element:
a. An integer containing value 789.

【中文翻译】
给定一个用字符串表示的嵌套整数列表，实现一个解析器来反序列化它。

每个元素要么是一个整数，要么是一个列表 —— 其元素也可能是整数或其他列表。

注意：
你可以假设字符串是格式良好的：

字符串非空。

字符串不包含空格。

字符串只包含数字 `0-9`、`[`、`-`、`,`、`]`。

示例 1：

给定 s = "324"，

你应该返回一个包含单个整数 324 的 NestedInteger 对象。

示例 2：

给定 s = "[123,[456,[789]]]"，

返回一个包含 2 个元素的嵌套列表的 NestedInteger 对象：

1. 一个包含值 123 的整数。
2. 一个包含两个元素的嵌套列表：
   i.  一个包含值 456 的整数。
   ii. 一个包含一个元素的嵌套列表：
       a. 一个包含值 789 的整数。
"""

from typing import List, Optional


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ''
        for ch in s:
            if ch == '[':
                stack.append(NestedInteger())
            elif ch == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                completed = stack.pop()
                if stack:
                    stack[-1].add(completed)
                else:
                    return completed
            elif ch == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
            else:
                num += ch
        return None  # unreachable for well-formed input











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈来模拟嵌套结构。
# 1. 如果字符串不以 '[' 开头，说明是一个单纯的数字，直接返回包装后的 NestedInteger。
# 2. 遍历字符串的每个字符：
#    - 遇到 '['：创建一个新的 NestedInteger 列表对象并入栈。
#    - 遇到数字或 '-'：累积到 num 字符串中（处理多位数和负数）。
#    - 遇到 ',' 或 ']'：如果 num 不为空，将累积的数字包装成 NestedInteger 并添加到栈顶列表中，
#      然后清空 num。如果是 ']'，还要弹出栈顶已完成解析的列表：如果栈非空，
#      将其添加到新的栈顶列表中；如果栈为空，说明是最外层，直接返回。
# 这种方法可以处理任意深度的嵌套列表。
#
# 时间复杂度: O(n) - 遍历字符串一次，n 为字符串长度
# 空间复杂度: O(d + m) - 栈空间取决于嵌套深度 d，以及数字字符串 num 的长度 m
#
# 关键点:
# - 使用栈处理嵌套结构，类似括号匹配问题
# - 需要处理负数和多位数，使用字符串累积数字
# - 遇到逗号或括号时提交累积的数字
# - 注意最外层和非嵌套输入的边界情况
