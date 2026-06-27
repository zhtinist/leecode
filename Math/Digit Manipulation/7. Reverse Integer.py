"""
LeetCode #7 - Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers.
"""


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        result = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow BEFORE multiplying/appending
            if result > INT_MAX // 10:
                return 0
            if result == INT_MAX // 10 and digit > 7:
                return 0

            result = result * 10 + digit

        return sign * result
