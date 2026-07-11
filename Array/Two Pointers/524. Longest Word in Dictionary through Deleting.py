"""
LeetCode #524 - Longest Word in Dictionary through Deleting
中文题名：通过删除字母匹配到字典里最长单词
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

Given a string and a string dictionary, find the longest string in the dictionary that can
be formed by deleting some characters of the given string. If there are more than one
possible results, return the longest word with the smallest lexicographical order. If there
is no possible result, return the empty string.

Example 1:

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

Example 2:

Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"

Note:

All the strings in the input will only contain lower-case letters.

The size of the dictionary won't exceed 1,000.

The length of all the strings in the input won't exceed 1,000.

【中文翻译】
给定一个字符串 s 和一个字符串字典 d，找到字典中可以通过删除 s 中某些字符形成的最长字符串。
如果有多个可能的结果，返回长度最长且字典序最小的单词。如果没有可能的结果，返回空字符串。

示例 1：
    输入：s = "abpcplea", d = ["ale","apple","monkey","plea"]
    输出："apple"

示例 2：
    输入：s = "abpcplea", d = ["a","b","c"]
    输出："a"

说明：所有输入字符串仅包含小写字母。字典大小不超过 1000。所有字符串长度不超过 1000。
"""

from typing import List, Optional


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # Sort: longest first, then lexicographical order
        d.sort(key=lambda x: (-len(x), x))

        for word in d:
            if self._is_subsequence(word, s):
                return word
        return ""

    def _is_subsequence(self, word: str, s: str) -> bool:
        """Check if word is a subsequence of s using two pointers."""
        i = 0
        for ch in s:
            if i < len(word) and word[i] == ch:
                i += 1
        return i == len(word)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 首先对字典按长度降序、同长度按字典序升序排序。然后依次判断每个单词是否为 s 的子序列
# （通过删除 s 中字符得到）。使用双指针法判断子序列：遍历 s，若当前字符匹配目标单词的当前
# 字符，则移动单词指针。若能匹配完整个单词则返回该单词。由于已排序，第一个匹配成功的即答案。
#
# 时间复杂度: O(N * logN + N * L) — N 为字典大小（排序），L 为 s 的长度（每个单词双指针检查）
# 空间复杂度: O(N) — 排序所需空间（Python 排序为 Timsort，需额外空间）
#
# 关键点:
# - 排序策略：先按长度降序再按字典序升序，保证第一个成功匹配即为答案
# - 双指针判断子序列是 O(L) 的线性扫描
# - 可以不排序而是遍历字典并维护当前最优结果，每次比较长度和字典序，避免排序开销
