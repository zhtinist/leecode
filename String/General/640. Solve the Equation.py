"""
LeetCode #640 - Solve the Equation
中文题名：求解方程
https://leetcode.com/problems/solve-the-equation/

Solve a given equation and return the value of `x` in the form of string
"x=#value". The equation contains only '+', '-' operation, the variable `x` and
its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of
`x` is an integer.

Example 1:

Input: "x+5-3+x=6+x-2"
Output: "x=2"

Example 2:

Input: "x=x"
Output: "Infinite solutions"

Example 3:

Input: "2x=x"
Output: "x=0"

Example 4:

Input: "2x+3x-6x=x+2"
Output: "x=-1"

Example 5:

Input: "x=x+2"
Output: "No solution"

【中文翻译】
求解一个给定的方程，将 `x` 的值以 "x=#value" 的字符串形式返回。
方程仅包含 '+'、'-' 操作、变量 `x` 及其系数。

如果方程没有解，返回 "No solution"。

如果方程有无穷多解，返回 "Infinite solutions"。

如果方程恰好有一个解，我们保证 `x` 的值是一个整数。

示例 1：

输入："x+5-3+x=6+x-2"
输出："x=2"

示例 2：

输入："x=x"
输出："Infinite solutions"

示例 3：

输入："2x=x"
输出："x=0"

示例 4：

输入："2x+3x-6x=x+2"
输出："x=-1"

示例 5：

输入："x=x+2"
输出："No solution"
"""

from typing import List, Optional


class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr: str) -> tuple[int, int]:
            """Parse an expression and return (coefficient_of_x, constant)."""
            coeff_x = 0
            const = 0
            num = 0
            sign = 1  # 1 for +, -1 for -
            i = 0

            while i < len(expr):
                ch = expr[i]
                if ch == 'x':
                    # Handle cases like "x", "+x", "-x"
                    if i == 0 or expr[i - 1] in '+-':
                        coeff_x += sign
                    else:
                        coeff_x += sign * num
                    num = 0
                elif ch == '+':
                    const += sign * num
                    num = 0
                    sign = 1
                elif ch == '-':
                    const += sign * num
                    num = 0
                    sign = -1
                else:
                    num = num * 10 + int(ch)
                i += 1

            const += sign * num  # Add the last number
            return coeff_x, const

        left, right = equation.split('=')
        left_x, left_c = parse(left)
        right_x, right_c = parse(right)

        # Move x terms to left, constants to right
        coeff_x = left_x - right_x
        const = right_c - left_c

        if coeff_x == 0:
            if const == 0:
                return "Infinite solutions"
            return "No solution"

        return f"x={const // coeff_x}"



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将方程分成等号左右两部分，分别解析每一侧的表达式：
# 1. 编写 parse 函数，遍历表达式字符串的每个字符。
# 2. 维护 sign（符号）、num（当前数字）、coeff_x（x 系数和）、const（常数和）。
# 3. 遇到 'x'：如果前面是符号或无数字（如 "+x" 或 "x"），系数为 sign * 1；
#    否则系数为 sign * num。
# 4. 遇到 '+'、'-'：将当前符号*数字累加到 const，重置 num，更新 sign。
# 5. 遇到数字：累积到 num。
# 6. 分别得到左侧和右侧的 x 系数与常数后，将 x 移项到左边、常数移项到右边：
#    最终方程变为 coeff_x * x = const。
# 7. 若 coeff_x == 0 且 const == 0：无穷解；coeff_x == 0 且 const != 0：无解。
#    否则 x = const // coeff_x（题目保证整数解）。
#
# 时间复杂度: O(N) - N 为方程字符串长度
# 空间复杂度: O(1) - 只使用常数额外变量
#
# 关键点:
# - 处理无数字前缀的 x（如 "x"、"+x"、"-x"）
# - 处理最后一个数字（循环结束后要加上最后的符号*数字）
# - 移项：左侧 x 系数 - 右侧 x 系数，右侧常数 - 左侧常数
# - 整数除法 // 是因为题目保证 x 是整数
