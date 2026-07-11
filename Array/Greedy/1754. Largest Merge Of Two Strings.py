"""
LeetCode #1754 - Largest Merge Of Two Strings
中文题名：构造字典序最大的合并字符串
https://leetcode.com/problems/largest-merge-of-two-strings/

You are given two strings `word1` and `word2`. You want to construct a string `merge` in the following way: while either `word1` or `word2` are non-empty, choose one of the following options:

If `word1` is non-empty, append the first character in `word1` to `merge` and delete it from `word1`.

For example, if `word1 = "abc" `and `merge = "dv"`, then after choosing this operation, `word1 = "bc"` and `merge = "dva"`.

If `word2` is non-empty, append the first character in `word2` to `merge` and delete it from `word2`.

For example, if `word2 = "abc" `and `merge = ""`, then after choosing this operation, `word2 = "bc"` and `merge = "a"`.

Return the lexicographically largest `merge` you can construct.

A string `a` is lexicographically larger than a string `b` (of the same length) if in the first position where `a` and `b` differ, `a` has a character strictly larger than the corresponding character in `b`. For example, `"abcd"` is lexicographically larger than `"abcc"` because the first position they differ is at the fourth character, and `d` is greater than `c`.

Example 1:

Input: word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"
Explanation: One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.

Example 2:

Input: word1 = "abcabc", word2 = "abdcaba"
Output: "abdcabcabcaba"

Constraints:

`1 <= word1.length, word2.length <= 3000`

`word1` and `word2` consist only of lowercase English letters.

【中文翻译】
给定两个字符串 word1 和 word2。每次操作可以从 word1 或 word2 的开头取一个字符，加入结果字符串尾部。
返回可以构造的字典序最大的结果字符串。

示例 1：
输入: word1 = "cabaa", word2 = "bcaaa"
输出: "cbcabaaaaa"
解释: 合并过程：取c(w1)→c; 比较w1["abaa"]和w2["bcaaa"]，w2字典序大，取b→cb; 继续取w2的c→cbc; 比较w1["abaa"]和w2["aaa"]，w1大...
"""

from typing import List, Optional


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        m, n = len(word1), len(word2)
        result = []

        while i < m and j < n:
            # 比较剩余子串的字典序
            if word1[i:] > word2[j:]:
                result.append(word1[i])
                i += 1
            else:
                result.append(word2[j])
                j += 1

        result.append(word1[i:])
        result.append(word2[j:])
        return ''.join(result)
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心法。每次比较两个字符串剩余部分的字典序，选择字典序更大的字符串的第一个字符。
# 这是正确的因为接下来要构造的字符串的字典序取决于最早的决定——
# 只要选择当前剩余串较大的那个，就能保证得到最大的最终结果。
# 注意比较的是整个剩余子串，而不仅仅是当前字符（因为相等字符需要看后续决定）。
#
# 时间复杂度: O((M+N)^2) — 字符串切片比较是 O(M+N)
# 空间复杂度: O(M+N) — 结果字符串
#
# 关键点:
# - 比较剩余整个子串而非单个字符（当前字符相同时看后面）
# - Python 的字符串切片比较自动按字典序
# - 贪心的正确性基于局部最优选择能导出全局最优
