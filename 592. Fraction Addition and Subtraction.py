"""
LeetCode #592 - Fraction Addition and Subtraction
中文题名：分数加减运算
https://leetcode.com/problems/fraction-addition-and-subtraction/

Given a string representing an expression of fraction addition and subtraction, you need to
return the calculation result in string format. The final result should be irreducible fraction.
If your final result is an integer, say `2`, you need to change it to the format
of fraction that has denominator `1`. So in this case, `2` should be
converted to `2/1`.

Example 1:

Input:"-1/2+1/2"
Output: "0/1"

Example 2:

Input:"-1/2+1/2+1/3"
Output: "1/3"

Example 3:

Input:"1/3-1/2"
Output: "-1/6"

Example 4:

Input:"5/3+1/3"
Output: "2/1"

Note:

The input string only contains `'0'` to `'9'`, `'/'`,
`'+'` and `'-'`. So does the output.

Each fraction (input and output) has format `±numerator/denominator`. If the
first input fraction or the output is positive, then `'+'` will be omitted.

The input only contains valid irreducible fractions, where the numerator
and denominator of each fraction will always be in the range [1,10]. If the
denominator is 1, it means this fraction is actually an integer in a fraction format
defined above.

The number of given fractions will be in the range [1,10].

The numerator and denominator of the final result are guaranteed to be valid and
in the range of 32-bit int.

【中文翻译】
给定一个表示分数加减运算的字符串，你需要以字符串格式返回计算结果。最终结果应为最简分数。
如果最终结果是整数，比如 `2`，需要将其转换为分母为 `1` 的分数格式。因此这种情况下，
`2` 应转换为 `2/1`。

示例 1：
    输入："-1/2+1/2"
    输出："0/1"

示例 2：
    输入："-1/2+1/2+1/3"
    输出："1/3"

示例 3：
    输入："1/3-1/2"
    输出："-1/6"

示例 4：
    输入："5/3+1/3"
    输出："2/1"

注意：
    输入字符串只包含 `'0'` 到 `'9'`、`'/'`、`'+'` 和 `'-'`。输出同理。
    每个分数的格式为 `±分子/分母`。如果第一个输入分数或输出为正，则省略 `'+'`。
    输入只包含有效的最简分数，每个分数的分子和分母在 [1, 10] 范围内。如果分母为 1，
    表示该分数实际上是一个整数按上述格式表示。
    给定分数的数量在 [1, 10] 范围内。
    最终结果的分子和分母保证有效且在 32 位整数范围内。
"""

from typing import List, Optional
import math
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        """
        Parse all fractions, compute a common denominator, sum the numerators,
        then reduce by GCD.
        """
        # Parse all +/- fraction tokens
        tokens = re.findall(r"[+-]?\d+/\d+", expression)

        # Initialize result numerator and denominator
        num, den = 0, 1  # 0/1

        for token in tokens:
            n_str, d_str = token.split("/")
            n, d = int(n_str), int(d_str)
            # Cross-multiply to add: num/den + n/d = (num*d + n*den) / (den*d)
            num = num * d + n * den
            den = den * d

        # Simplify by dividing numerator and denominator by their GCD
        g = math.gcd(num, den)
        num //= g
        den //= g

        # Ensure denominator is positive
        if den < 0:
            num = -num
            den = -den

        return f"{num}/{den}"



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用正则表达式解析输入字符串中的所有分数（形如 "+a/b" 或 "-a/b"）。维护
# num/den 表示当前累计结果（初始 0/1）。遍历每个解析出的分数 a/b，通过通分相加：
# num/den + a/b = (num*b + a*den) / (den*b)。全部累加完后，用 math.gcd 对
# 分子分母约分化简，并确保分母为正数。最后返回 "num/den" 格式的字符串。
#
# 时间复杂度: O(K) — K 为分数的个数（最多 10），每次通分 O(1)
# 空间复杂度: O(K) — 存储解析出的分数 tokens
#
# 关键点:
# - 正则表达式 `[+-]?\d+/\d+` 正确解析每个带符号的分数
# - 通分公式：a/b + c/d = (a*d + c*b) / (b*d)
# - 最终用 math.gcd 化简，注意分母可能为负的情况
