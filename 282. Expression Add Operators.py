"""
LeetCode #282 - Expression Add Operators
https://leetcode.com/problems/expression-add-operators/

Given a string that contains only digits `0-9` and a target value, return all
possibilities to add binary operators (not unary) `+`, `-`, or
`*` between the digits so they evaluate to the target value.

Example 1:

Input: `*num* = `"123", *target* = 6
Output: ["1+2+3", "1*2*3"]

Example 2:

Input: `*num* = `"232", *target* = 8
Output: ["2*3+2", "2+3*2"]

Example 3:

Input: `*num* = `"105", *target* = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: `*num* = `"00", *target* = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:

Input: `*num* = `"3456237490", *target* = 9191
Output: []
"""

from typing import List, Optional


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """Return all possibilities to add +, -, * operators to num to reach target.

        Backtracking with parameters:
        - index: current position in num
        - prev_operand: the last operand (needed for * precedence)
        - cur_val: current evaluated value
        - expr: expression string built so far
        """
        result = []
        n = len(num)

        def backtrack(index: int, prev_operand: int, cur_val: int, expr: str):
            if index == n:
                if cur_val == target:
                    result.append(expr)
                return

            # Try all possible numbers starting at index
            for i in range(index, n):
                # Skip numbers with leading zero (e.g., "05" is invalid)
                if i > index and num[index] == '0':
                    break

                cur_str = num[index:i + 1]
                cur_num = int(cur_str)

                if index == 0:
                    # First number: no operator before it
                    backtrack(i + 1, cur_num, cur_num, cur_str)
                else:
                    # Addition
                    backtrack(i + 1, cur_num, cur_val + cur_num, expr + '+' + cur_str)
                    # Subtraction
                    backtrack(i + 1, -cur_num, cur_val - cur_num, expr + '-' + cur_str)
                    # Multiplication: need to undo previous operation and re-apply
                    # cur_val - prev_operand + prev_operand * cur_num
                    backtrack(i + 1, prev_operand * cur_num,
                              cur_val - prev_operand + prev_operand * cur_num,
                              expr + '*' + cur_str)

        backtrack(0, 0, 0, "")
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 回溯法（Backtracking）。在每个位置，我们有三种选择：+、-、*（第一个数字前没有运算符）。
# 对于加法和减法，直接更新当前值即可。对于乘法，需要特殊处理，因为乘法的优先级
# 高于加减法。我们需要记录上一个操作数（prev_operand），在遇到乘法时：
# 先将上一个操作数从当前值中撤销（cur_val - prev_operand），
# 然后加上 (prev_operand * cur_num)。
# 同时需要注意跳过前导零的数字（如 "05" 不合法）。
#
# 时间复杂度: O(4^N) - 每个位置有 4 种选择（无运算符、+、-、*），N 为数字长度
# 空间复杂度: O(N) - 递归深度和表达式字符串长度
#
# 关键点:
# - 乘法的优先级处理：需要 prev_operand 来回退上一个操作
# - 前导零检查：如果 num[index] == '0' 且 i > index，跳过（不允许 "05" 这样的数字）
# - 回溯的参数设计：index, prev_operand, cur_val, expr
# - 第一个数字前不能有运算符，需要特殊处理
