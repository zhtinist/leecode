"""
LeetCode #76 - Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string "".

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

Example 2:
    Input: s = "a", t = "a"
    Output: "a"

Example 3:
    Input: s = "a", t = "aa"
    Output: ""

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 10^5
    s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        start = 0
        length = float("inf")

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if right - left + 1 < length:
                    start = left
                    length = right - left + 1

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if length == float("inf") else s[start : start + length]
