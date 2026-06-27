"""
LeetCode #14 - Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.longestCommonPrefix_vertical(strs)

    def longestCommonPrefix_vertical(self, strs: List[str]) -> str:
        """
        Vertical scan: compare character by character at the same index.
        Time O(n * m), Space O(1) — n = number of strings, m = shortest length.
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]

    def longestCommonPrefix_horizontal(self, strs: List[str]) -> str:
        """
        Horizontal scan: start from the first string and shrink prefix until
        every string starts with it.
        Time O(n * m) ~ O(n * L^2) worst case, Space O(1).
        """
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
