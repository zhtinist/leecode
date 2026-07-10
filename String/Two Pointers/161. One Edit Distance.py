"""
LeetCode #161 - One Edit Distance
https://leetcode.com/problems/one-edit-distance/

Given two strings s and t, return true if they are both one edit distance apart,
false otherwise.

A string s is said to be one edit distance apart from a string t if you can:
- Insert exactly one character into s to get t.
- Delete exactly one character from s to get t.
- Replace exactly one character of s with a different character to get t.

Example 1:
    Input: s = "ab", t = "acb"
    Output: true
    Explanation: We can insert 'c' into s to get t.

Example 2:
    Input: s = "cab", t = "ad"
    Output: false
    Explanation: We cannot get t from s by only one edit.

Constraints:
    0 <= s.length, t.length <= 10^4
    s and t consist of lowercase letters, uppercase letters, and digits.
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) > len(t):
            s, t = t, s

        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i + 1 :] == t[i + 1 :]
                return s[i:] == t[i + 1 :]

        return len(s) + 1 == len(t)
