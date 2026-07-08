"""
LeetCode #91 - Decode Ways
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z can be encoded into numbers using the
mapping 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".

Given a string s containing only digits, return the number of ways to decode it.

Example 1:
    Input: s = "12"
    Output: 2

Example 2:
    Input: s = "226"
    Output: 3

Example 3:
    Input: s = "06"
    Output: 0

Constraints:
    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            two_digit = int(s[i - 2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
