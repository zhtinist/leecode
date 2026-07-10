"""
LeetCode #227 - Basic Calculator II
中文题名：基本计算器 II
https://leetcode.com/problems/basic-calculator-ii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, `+`,
`-`, `*`, `/` operators and empty spaces ` `.
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:

You may assume that the given expression is always valid.

Do not use the `eval` built-in library function.

【中文翻译】
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数、`+`、`-`、`*`、`/` 运算符和空格 ` `。整数除法应截断向零取整。

示例 1：

输入："3+2*2"
输出：7

示例 2：

输入：" 3/2 "
输出：1

示例 3：

输入：" 3+5 / 2 "
输出：5

注意：

你可以假设所给表达式是有效的。

不要使用内置的 `eval` 库函数。
"""

from typing import List, Optional


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_op = '+'

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch in '+-*/' or i == len(s) - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / num))
                prev_op = ch
                num = 0

        return sum(stack)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 没有括号，但需要处理 * 和 / 的优先级。使用栈来延迟计算:
# 维护变量 prev_op 记录前一个运算符，num 记录当前数字。
# 遍历字符串:
# - 遇到数字: 累积到 num
# - 遇到运算符或到达字符串末尾: 根据 prev_op 决定如何入栈:
#   - '+': 直接入栈 num
#   - '-': 入栈 -num (用负数表示减法)
#   - '*': 弹出栈顶，与 num 相乘后入栈
#   - '/': 弹出栈顶，除以 num 后入栈 (使用 int() 实现向零截断)
# - 更新 prev_op 为当前运算符，重置 num = 0
# 最后栈中所有元素求和即为结果。
#
# 时间复杂度: O(n) - 每个字符处理一次
# 空间复杂度: O(n) - 栈在最坏情况下(全加减法)存储 O(n) 个元素
#
# 关键点:
# - 乘除法立即计算并入栈，加减法延迟到遍历结束后统一求和
# - 除法用 int(stack.pop() / num) 确保向零截断(Python 中 / 是浮点除法)
# - 注意遍历到末尾时也要触发一次运算(i == len(s)-1)
# - 空格被忽略，不影响解析
