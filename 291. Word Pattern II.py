"""
LeetCode #291 - Word Pattern II
https://leetcode.com/problems/word-pattern-ii/

Given a `pattern` and a string `str`, find if `str` follows
the same pattern.

Here follow means a full match, such that there is a bijection between a letter in
`pattern` and a non-empty substring in `str`.

Example 1:

Input: pattern = `"abab"`, str = `"redblueredblue"`
Output: true

Example 2:

Input: pattern = pattern = `"aaaa"`, str = `"asdasdasdasd"`
Output: true

Example 3:

Input: pattern = `"aabb"`, str = `"xyzabcxzyabc"`
Output: false

Notes:

You may assume both `pattern` and `str` contains only lowercase
letters.
"""

from typing import List, Optional


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        """Check if string s matches pattern with bijection using backtracking.

        Similar to Word Pattern but we need to try all possible splits of s.
        Backtracking: for each pattern character, try all possible substrings
        of s starting at current position.
        """
        char_to_word = {}
        word_to_char = set()

        def backtrack(p_idx: int, s_idx: int) -> bool:
            """Try to match pattern[p_idx:] with s[s_idx:]."""
            if p_idx == len(pattern) and s_idx == len(s):
                return True
            if p_idx == len(pattern) or s_idx == len(s):
                return False

            ch = pattern[p_idx]

            # If this pattern char is already mapped
            if ch in char_to_word:
                word = char_to_word[ch]
                # Check if s starting at s_idx begins with this word
                if s[s_idx:s_idx + len(word)] == word:
                    return backtrack(p_idx + 1, s_idx + len(word))
                return False

            # Try mapping ch to every possible substring starting at s_idx
            for end in range(s_idx + 1, len(s) + 1):
                candidate = s[s_idx:end]
                if candidate in word_to_char:
                    continue
                # Prune: remaining characters must be enough
                remaining_pattern = len(pattern) - p_idx - 1
                remaining_str = len(s) - end
                if remaining_str < remaining_pattern:
                    break
                # Make the mapping
                char_to_word[ch] = candidate
                word_to_char.add(candidate)
                if backtrack(p_idx + 1, end):
                    return True
                # Backtrack
                del char_to_word[ch]
                word_to_char.remove(candidate)

            return False

        return backtrack(0, 0)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 回溯法（Backtracking）。与 #290 Word Pattern 不同，这里需要自己分割字符串 s。
# 对于 pattern 的每个字符，尝试将其映射到 s 中以当前位置开始的各种子串。
# 使用两个数据结构维护双向映射：char_to_word (ch->word) 和 word_to_char
# (用 set 记录已被映射的 word)。
# 剪枝条件：剩余字符串长度不能小于剩余 pattern 字符数（因为每个字符至少匹配一个字符）。
# 如果当前 pattern 字符已有映射，直接验证并跳过。
#
# 时间复杂度: O(M * 2^N) - M 为 pattern 长度，N 为 s 长度（指数级但带剪枝）
# 空间复杂度: O(M + N) - 递归栈深度和哈希表大小
#
# 关键点:
# - 与 #290 不同，需要自己分割字符串，因此需要回溯
# - 双射检查：char->word 和 word->char 两个方向
# - 剪枝优化：剩余字符串长度 >= 剩余 pattern 字符数
# - 如果 pattern 字符已有映射，直接跳过尝试阶段
