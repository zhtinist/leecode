"""
LeetCode #132 - Palindrome Partitioning II
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a
palindrome. Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
    Input: s = "aab"
    Output: 1

Example 2:
    Input: s = "a"
    Output: 0

Example 3:
    Input: s = "ab"
    Output: 1

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase English letters only.
"""


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end, -1, -1):
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True

        dp = [0] * n
        for end in range(n):
            if is_palindrome[0][end]:
                dp[end] = 0
            else:
                dp[end] = end
                for start in range(1, end + 1):
                    if is_palindrome[start][end]:
                        dp[end] = min(dp[end], dp[start - 1] + 1)

        return dp[n - 1]
