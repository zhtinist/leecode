"""
LeetCode #290 - Word Pattern
https://leetcode.com/problems/word-pattern/

Given a `pattern` and a string `str`, find if `str` follows
the same pattern.

Here follow means a full match, such that there is a bijection between a letter in
`pattern` and a non-empty word in `str`.

Example 1:

Input: pattern = `"abba"`, str = `"dog cat cat dog"`
Output: true

Example 2:

Input:pattern = `"abba"`, str = `"dog cat cat fish"`
Output: false

Example 3:

Input: pattern = `"aaaa"`, str = `"dog cat cat dog"`
Output: false

Example 4:

Input: pattern = `"abba"`, str = `"dog dog dog dog"`
Output: false

Notes:

You may assume `pattern` contains only lowercase letters, and `str`
contains lowercase letters that may be separated by a single space.
"""

from typing import List, Optional


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Check if string s follows the same pattern as pattern.

        Bijection check: each character in pattern maps to exactly one word in s,
        and each word in s maps to exactly one character in pattern.
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for ch, word in zip(pattern, words):
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                char_to_word[ch] = word

            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            else:
                word_to_char[word] = ch

        return True


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 双射（Bijection）检查。需要同时检查两个方向的映射：
# 1. 模式字符 -> 单词：同一个字符必须始终映射到同一个单词
# 2. 单词 -> 模式字符：同一个单词必须始终映射到同一个字符
#
# 首先按空格分割 s 得到单词列表，如果单词数量与模式长度不匹配，直接返回 False。
# 然后同时遍历 pattern 和 words，用两个哈希表分别记录两个方向的映射。
# 如果发现映射冲突（同一个 key 映射到不同的 value），返回 False。
#
# 时间复杂度: O(N) - 遍历一遍，N 为单词数
# 空间复杂度: O(N) - 两个哈希表存储映射关系
#
# 关键点:
# - 双射要求两个方向的映射都唯一
# - 两个哈希表分别检查 ch->word 和 word->ch
# - 长度不匹配的情况要提前处理
# - 与 #205 Isomorphic Strings 是同类问题
