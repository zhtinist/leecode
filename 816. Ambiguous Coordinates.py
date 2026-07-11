"""
LeetCode #816 - Ambiguous Coordinates
中文题名：模糊坐标
https://leetcode.com/problems/ambiguous-coordinates/

We had some 2-dimensional coordinates, like `"(1, 3)"` or `"(2,
0.5)"`.  Then, we removed all commas, decimal points, and spaces, and
ended up with the string `S`.  Return a list of strings representing all
possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers
like "00", "0.0", "0.00", "1.0", "001",
"00.01", or any other number that can be represented with less digits.
Also, a decimal point within a number never occurs without at least one digit occuring
before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in
the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

Example 2:
Input: "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation:
0.0, 00, 0001 or 00.01 are not allowed.

Example 3:
Input: "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

Example 4:
Input: "(100)"
Output: [(10, 0)]
Explanation:
1.0 is not allowed.

Note:

`4 <= S.length <= 12`.

`S[0]` = "(", `S[S.length - 1]` = ")", and the
other elements in `S` are digits.

【中文翻译】
我们有一些二维坐标，如 `"(1, 3)"` 或 `"(2, 0.5)"`。然后我们删除了所有的逗号、小数点和空格，得到了字符串 `S`。返回一个字符串列表，表示原始坐标可能的所有形式。

原始表示从不包含多余的零，所以我们永远不会以 "00"、"0.0"、"0.00"、"1.0"、"001"、"00.01" 或任何可用更少位数表示的数字开头。另外，小数点前至少有一个数字，所以我们永远不会以 ".1" 这样的数字开头。

最终答案列表可以按任意顺序返回。注意，最终答案中的所有坐标在逗号后都恰好有一个空格。

示例 1：
输入："(123)"
输出：["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

示例 2：
输入："(00011)"
输出：["(0.001, 1)", "(0, 0.011)"]
解释：0.0、00、0001 或 00.01 不被允许。

示例 3：
输入："(0123)"
输出：["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

示例 4：
输入："(100)"
输出：[(10, 0)]
解释：1.0 不被允许。

注意：
`4 <= S.length <= 12`。
`S[0]` = "("，`S[S.length - 1]` = ")"，S 中的其他元素是数字。
"""

from typing import List, Optional


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def valid_numbers(digits: str) -> List[str]:
            """Generate all valid numbers from a digit string."""
            n = len(digits)
            if n == 1:
                return [digits]

            results = []
            # Integer form: no leading zero unless it's exactly "0"
            if digits[0] != '0':
                results.append(digits)

            # Decimal form: s[:i] + '.' + s[i:]
            for i in range(1, n):
                integer_part = digits[:i]
                fractional_part = digits[i:]
                # Integer part must be valid (no leading zero unless single "0")
                if len(integer_part) > 1 and integer_part[0] == '0':
                    continue
                # Fractional part must not end with '0'
                if fractional_part[-1] == '0':
                    continue
                results.append(integer_part + '.' + fractional_part)
            return results

        # Remove parentheses
        digits = s[1:-1]
        n = len(digits)
        result = []

        # Split at every position
        for split in range(1, n):
            left_digits = digits[:split]
            right_digits = digits[split:]
            left_nums = valid_numbers(left_digits)
            right_nums = valid_numbers(right_digits)
            for l in left_nums:
                for r in right_nums:
                    result.append(f"({l}, {r})")

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 去掉 S 的括号，得到纯数字字符串 digits。
# 2. 枚举所有分割点（1 到 n-1），将 digits 分为左右两部分。
# 3. 对于每部分，生成所有合法的数字表示：
#    - 整数形式：无前导零（除非是单个 "0"）
#    - 小数形式：整数部分无前导零（除非是单个 "0"），
#      小数部分不以 '0' 结尾
# 4. 将左右两部分的合法数字表示进行笛卡尔积组合，
#    格式化为 "(left, right)"。
#
# 时间复杂度: O(N^3) - N 为字符串长度（<= 10）。
#   最坏情况：O(N) 分割点 * O(N^2) 合法数字组合
# 空间复杂度: O(N^3) - 存储所有结果
#
# 关键点:
# - 整数部分不能有前导零（"0"本身除外）
# - 小数部分不能以 '0' 结尾
# - 每个分割的两部分都需要独立生成合法数字列表
# - N 很小（<= 10），穷举完全可行
