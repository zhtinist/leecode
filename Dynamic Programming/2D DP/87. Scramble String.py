"""
LeetCode #87 - Scramble String
https://leetcode.com/problems/scramble-string/

Given a string s1 and a string s2, return true if s2 is a scrambled string of s1,
or false otherwise.

Example 1:
    Input: s1 = "great", s2 = "rgeat"
    Output: true

Example 2:
    Input: s1 = "abcde", s2 = "caebd"
    Output: false

Example 3:
    Input: s1 = "a", s2 = "a"
    Output: true

Constraints:
    s1.length == s2.length
    1 <= s1.length <= 30
    s1 and s2 consist of lowercase English letters.
"""

from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)
        def dfs(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False

            n = len(a)
            for i in range(1, n):
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True
                if dfs(a[:i], b[n - i :]) and dfs(a[i:], b[: n - i]):
                    return True
            return False

        return dfs(s1, s2)
