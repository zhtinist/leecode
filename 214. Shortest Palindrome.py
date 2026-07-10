"""
LeetCode #214 - Shortest Palindrome
中文题名：最短回文串
https://leetcode.com/problems/shortest-palindrome/

Given a string *s*, you are allowed to convert it to a palindrome by adding
characters in front of it. Find and return the shortest palindrome you can find by
performing this transformation.

Example 1:

Input: `"aacecaaa"`
Output: `"aaacecaaa"`

Example 2:

Input: `"abcd"`
Output: `"dcbabcd"`

【中文翻译】
给定一个字符串 *s*，你可以通过在字符串前面添加字符来将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1：

输入：`"aacecaaa"`
输出：`"aaacecaaa"`

示例 2：

输入：`"abcd"`
输出：`"dcbabcd"`
"""

from typing import List, Optional


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Build combined string: s + '#' + reverse(s)
        rev = s[::-1]
        combined = s + '#' + rev

        # Compute LPS (Longest Prefix Suffix) array using KMP
        n = len(combined)
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j

        # lps[-1] is the length of the longest palindromic prefix of s
        # Prepend the non-palindromic suffix (reversed) to s
        return rev[:len(s) - lps[-1]] + s


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 使用 KMP 算法的 LPS（最长相同前后缀）数组来找到 s 的最长回文前缀。
# 1. 构造字符串 combined = s + '#' + reverse(s)，其中 '#' 是分隔符防止跨越连接。
# 2. 计算 combined 的 LPS 数组。
#    LPS[i] 表示 combined[0..i] 的最长相同前后缀长度。
#    例如 "aacecaaa#aaacecaa" 的最长前后缀为 "aacecaa"，长度 7。
# 3. LPS 的最后一个值即为 s 的最长回文前缀长度。
#    原理：s 的前缀与 reverse(s) 的后缀匹配（即 s 的回文前缀部分）。
# 4. 将 s 中非回文前缀的后缀部分翻转后添加到 s 前面，得到最短回文串。
#    即 reverse(s)[:len(s) - lps[-1]] + s。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - KMP LPS 数组找到字符串的最长回文前缀，是本题核心技巧
# - '#' 分隔符确保前缀不会跨越到反转部分产生错误的跨段匹配
# - 最终答案 = rev[:len(s) - lps[-1]] + s，巧妙利用了 LPS 的含义
