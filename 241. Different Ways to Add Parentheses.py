"""
LeetCode #241 - Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/

Given a string of numbers and operators, return all possible results from computing all the
different possible ways to group numbers and operators. The valid operators are
`+`, `-` and `*`.

Example 1:

Input: `"2-1-1"`
Output: `[0, 2]`
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:

Input: `"2*3-4*5"`
Output: `[-34, -14, -10, -10, 10]`
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""

from typing import List, Optional


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 记忆化递归，避免重复计算
        memo = {}

        def compute(expr: str) -> List[int]:
            if expr in memo:
                return memo[expr]

            # 如果表达式是纯数字，直接返回
            if expr.isdigit():
                return [int(expr)]

            res = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    # 分治：以当前运算符为界，分别计算左右两边所有可能的结果
                    left = compute(expr[:i])
                    right = compute(expr[i + 1:])
                    for l in left:
                        for r in right:
                            if ch == '+':
                                res.append(l + r)
                            elif ch == '-':
                                res.append(l - r)
                            else:  # '*'
                                res.append(l * r)
            memo[expr] = res
            return res

        return compute(expression)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路：
# 使用分治法（Divide and Conquer）+ 记忆化搜索。对于表达式中的每一个运算符，
# 将其作为"最后计算的运算符"，将表达式分成左右两部分。递归计算左右两部分各自
# 可能产生的所有结果，然后用当前运算符将左右结果两两组合。通过 memo 字典缓存
# 已计算过的子表达式结果，避免重复计算。
#
# 时间复杂度: O(n * 2^n) — 卡特兰数相关，n 个运算符产生的可能结果数
# 空间复杂度: O(n) — 递归栈深度 + memo 存储
#
# 关键点：
# - 以运算符为分界点进行分治
# - 记忆化避免重复计算相同子表达式
# - 纯数字（无运算符）作为递归终止条件
