"""
LeetCode #1638 - Count Substrings That Differ by One Character
中文题名：统计只差一个字符的子串数目
https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

Given two strings `s` and `t`, find the number of ways you can
choose a non-empty substring of `s` and replace a single
character by a different character such that the resulting substring is a
substring of `t`. In other words, find the number of substrings in
`s` that differ from some substring in `t` by
exactly one character.

For example, the underlined substrings in `"computer"` and
`"computation"` only differ by the
`'e'`/`'a'`, so this is a valid way.

Return the number of substrings that satisfy the condition above.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.

​​Example 2:

Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
​​​​The underlined portions are the substrings that are chosen from s and t.

Example 3:

Input: s = "a", t = "a"
Output: 0

Example 4:

Input: s = "abe", t = "bbc"
Output: 10

Constraints:

`1 <= s.length, t.length <= 100`

`s` and `t` consist of lowercase English letters only.

【中文翻译】
给定两个字符串 s 和 t。找出 s 的非空子串和 t 的非空子串中，恰好有一个字符不同的对数。
注意子串即连续字符序列。

示例 1：
输入: s = "aba", t = "baba"
输出: 6
解释: s 的多个子串与 t 的对应子串恰好有一个字符不同。
"""

from typing import List, Optional


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        ans = 0

        for i in range(m):
            for j in range(n):
                diff = 0
                k = 0
                while i + k < m and j + k < n:
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        ans += 1
                    if diff > 1:
                        break
                    k += 1

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 枚举所有对齐位置 (i, j)。从对齐位置开始同时向右扩展，维护不同字符计数 diff。
# 当 diff == 1 时，每扩展一个位置（只要 diff 仍为 1）就得到一个符合条件的子串对，ans++。
# 当 diff > 1 时停止该方向扩展。
#
# 时间复杂度: O(M * N * min(M,N)) — 最坏 O(M*N*(M+N))
# 空间复杂度: O(1)
#
# 关键点:
# - 枚举所有对齐位置，从对齐点同时向右扩展
# - diff == 1 时每个扩展位置都计一次，diff > 1 时停止
