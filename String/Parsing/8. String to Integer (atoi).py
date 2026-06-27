"""
LeetCode #8 - String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit
signed integer.

The algorithm for myAtoi(string s) is as follows:

1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or
   '+', assuming positivity if neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit
   character is encountered or the end of the string is reached. If no digits
   were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range
   [-2^31, 2^31 - 1], then round the integer to remain in the range.
   Specifically, integers less than -2^31 should be rounded to -2^31, and
   integers greater than 2^31 - 1 should be rounded to 2^31 - 1.

Return the integer as the final result.
"""


class Solution:
    INT_MIN = -(2 ** 31)
    INT_MAX = 2 ** 31 - 1

    def isDigit(self, c: str) -> bool:
        return c.isdigit()

    def delSpaces(self, s: str) -> str:
        return s.lstrip()

    def getSign(self, s: str) -> int:
        return -1 if s[0] == '-' else 1

    def myAtoi(self, s: str) -> int:
        s = self.delSpaces(s)
        if not s:
            return 0

        sign = self.getSign(s)
        if s[0] in '+-':
            s = s[1:]

        result = 0
        for c in s:
            if not self.isDigit(c):
                break
            result = result * 10 + int(c)

        result *= sign
        return max(self.INT_MIN, min(self.INT_MAX, result))


