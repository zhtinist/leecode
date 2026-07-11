"""
LeetCode #522 - Longest Uncommon Subsequence II
中文题名：最长特殊序列 II
https://leetcode.com/problems/longest-uncommon-subsequence-ii/

Given a list of strings, you need to find the longest uncommon subsequence among them. The
longest uncommon subsequence is defined as the longest subsequence of one of these strings
and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some
characters without changing the order of the remaining elements. Trivially, any string is a
subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest
uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:

Input: "aba", "cdc", "eae"
Output: 3

Note:

All the given strings' lengths will not exceed 10.

The length of the given list will be in the range of [2, 50].

【中文翻译】
给定一个字符串列表，需要找出其中最长的特殊序列。
最长特殊序列定义为：某个字符串的子序列，且不是任何其他字符串的子序列。

子序列可以通过删除某些字符而不改变其余字符的顺序来得到。
任何字符串都是其自身的子序列，空字符串是任何字符串的子序列。

输入为字符串列表，输出为最长特殊序列的长度。如果不存在，返回 -1。
"""

from typing import List, Optional


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(a: str, b: str) -> bool:
            """Return True if a is a subsequence of b."""
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)

        # Sort by length descending
        strs.sort(key=len, reverse=True)
        n = len(strs)

        for i in range(n):
            found = True
            for j in range(n):
                if i == j:
                    continue
                if is_subseq(strs[i], strs[j]):
                    found = False
                    break
            if found:
                return len(strs[i])
        return -1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键洞察：如果一个字符串不是任何其他字符串的子序列，那么该字符串本身就是一个"特殊序列"。
# 按长度降序排序，从最长的字符串开始检查。对于每个字符串，检查它是否是其他字符串的子序列。
# 如果不是，它的长度就是答案。如果所有字符串都是某个更长的字符串的子序列，则返回 -1。
# 注意：需要检查同长度字符串的重复情况（如果字符串自己出现了多次，它会是其他同值字符串的子序列）。
#
# 时间复杂度: O(n^2 * L) — n 个字符串，每对比较 O(L)，L<=10，最多 50 个字符串
# 空间复杂度: O(1) — 仅使用常数额外空间
#
# 关键点:
# - 整个字符串本身就是一个子序列（特殊序列）——题目核心洞察
# - 按长度降序保证第一个找到的就是最长的
# - 字符串本身的子序列关系是非自反的（除了与自己完全相等的情况）


