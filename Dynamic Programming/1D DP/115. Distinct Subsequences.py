"""
LeetCode #115 - Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/

Given two strings s and t, return the number of distinct subsequences of s which
equals t.

Example 1:
    Input: s = "rabbbit", t = "rabbit"
    Output: 3

Example 2:
    Input: s = "babgbag", t = "bag"
    Output: 5

Constraints:
    1 <= s.length, t.length <= 1000
    s and t consist of English letters.
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
