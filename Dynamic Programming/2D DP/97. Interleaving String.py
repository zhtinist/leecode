"""
LeetCode #97 - Interleaving String
https://leetcode.com/problems/interleaving-string/

Given strings s1, s2, and s3, return true if s3 is formed by an interleaving of
s1 and s2.

Example 1:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true

Example 2:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false

Example 3:
    Input: s1 = "", s2 = "", s3 = ""
    Output: true

Constraints:
    0 <= s1.length, s2.length <= 100
    s3.length == s1.length + s2.length
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        return dp[m][n]
