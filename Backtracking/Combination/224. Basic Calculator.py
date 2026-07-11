"""
LeetCode #224 - Basic Calculator
中文题名：基本计算器
https://leetcode.com/problems/basic-calculator/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `(` and closing parentheses `)`,
the plus `+` or minus sign `-`, non-negative integers and empty
spaces ` `.

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:

You may assume that the given expression is always valid.

Do not use the `eval` built-in library function.

【中文翻译】
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 `(` 和右括号 `)`，加号 `+` 或减号 `-`，非负整数和空格 ` `。

示例 1：

输入："1 + 1"
输出：2

示例 2：

输入：" 2-1 + 2 "
输出：3

示例 3：

输入："(1+(4+5+2)-3)+(6+8)"
输出：23

注意：

你可以假设所给表达式是有效的。

不要使用内置的 `eval` 库函数。
"""

from typing import List, Optional


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()

        result += sign * num
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 使用栈处理括号和符号。维护当前结果(result)、当前数字(num)和当前符号(sign)。
# 遍历字符串:
# - 遇到数字: 累积到 num (num = num * 10 + digit)
# - 遇到 '+' 或 '-': 将之前的数字(result += sign * num)结算到结果中，重置 num=0，
#   更新 sign=1(对于+)或 sign=-1(对于-)
# - 遇到 '(': 将当前的 result 和 sign 压入栈中保存，重置 result=0, sign=1 开始计算括号内的表达式
# - 遇到 ')': 先结算括号内最后的数字，然后将括号内的结果乘以栈顶的符号(sign before paren)，
#   再加上栈顶的结果(result before paren)
# 遍历结束后结算最后一个数字。
#
# 时间复杂度: O(n) - 每个字符处理一次
# 空间复杂度: O(n) - 栈在最坏情况下(全嵌套括号)存储 O(n) 个元素
#
# 关键点:
# - 栈中存储 (之前的result, 之前的sign) 元组，遇到 ')' 时恢复上下文
# - 符号 sign 用 1 和 -1 表示正负，避免字符串比较
# - 空格字符被忽略，不影响逻辑
