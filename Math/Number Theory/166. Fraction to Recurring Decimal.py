"""
LeetCode #166 - Fraction to Recurring Decimal
https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers numerator and denominator, return the fraction in string
format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
    Input: numerator = 1, denominator = 2
    Output: "0.5"

Example 2:
    Input: numerator = 2, denominator = 1
    Output: "2"

Example 3:
    Input: numerator = 4, denominator = 333
    Output: "0.(012)"

Constraints:
    -2^31 <= numerator, denominator <= 2^31 - 1
    denominator != 0
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        num, den = abs(numerator), abs(denominator)

        integer_part = num // den
        remainder = num % den

        if remainder == 0:
            return f"{sign}{integer_part}"

        result = [f"{sign}{integer_part}."]
        seen = {}

        while remainder:
            if remainder in seen:
                start = seen[remainder]
                result.insert(start, "(")
                result.append(")")
                break

            seen[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // den))
            remainder %= den

        return "".join(result)
