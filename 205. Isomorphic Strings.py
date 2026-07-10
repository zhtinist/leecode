"""
LeetCode #205 - Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/

Given two strings *s* and *t*, determine if they are isomorphic.

Two strings are isomorphic if the characters in *s* can be replaced to get *t*.

All occurrences of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character but a character may map
to itself.

Example 1:

Input: *s* = `"egg", `*t = *`"add"`
Output: true

Example 2:

Input: *s* = `"foo", `*t = *`"bar"`
Output: false

Example 3:

Input: *s* = `"paper", `*t = *`"title"`
Output: true

Note:

You may assume both *s *and *t *have the same length.
"""

from typing import List, Optional


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for cs, ct in zip(s, t):
            if cs in s_to_t:
                if s_to_t[cs] != ct:
                    return False
            else:
                s_to_t[cs] = ct

            if ct in t_to_s:
                if t_to_s[ct] != cs:
                    return False
            else:
                t_to_s[ct] = cs

        return True


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用两个哈希映射确保双射（bijection）关系。不只是 s -> t 的单向映射，
# 还需要 t -> s 的反向映射，因为题目要求"没有两个字符可以映射到同一个字符"。
#
# 遍历 s 和 t 的每一对字符 (cs, ct)：
# 1. 如果 cs 已映射，检查是否映射到当前的 ct，不是则返回 False
# 2. 如果 ct 已映射，检查是否映射到当前的 cs，不是则返回 False
# 3. 如果都没问题，建立双向映射
#
# 两个映射确保了"一一对应"：s 中不同的字符不能映射到 t 中相同的字符。
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(N) — 最多 256 个字符（ASCII），实际是 O(1)
#
# 关键点:
# - 必须使用双向映射，仅 s->t 不够
# - 例如 s="ab", t="cc"：单向映射 b->c 和 a->c 都成立，但 b 和 a 映射到同一字符
# - 另一种方法：比较两个字符串的编码模式（首次出现位置是否一致）
