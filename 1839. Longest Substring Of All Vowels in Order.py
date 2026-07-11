"""
LeetCode #1839 - Longest Substring Of All Vowels in Order
中文题名：所有元音按顺序排布的最长子字符串
https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

A string is considered beautiful if it satisfies the following conditions:

Each of the 5 English vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) must appear at least once in it.

The letters must be sorted in alphabetical order (i.e. all `'a'`s before `'e'`s, all `'e'`s before `'i'`s, etc.).

For example, strings `"aeiou"` and `"aaaaaaeiiiioou"` are considered beautiful, but `"uaeio"`, `"aeoiu"`, and `"aaaeeeooo"` are not beautiful.

Given a string `word` consisting of English vowels, return the length of the longest beautiful substring of `word`. If no such substring exists, return `0`.

A substring is a contiguous sequence of characters in a string.

Example 1:

Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.

Example 2:

Input: word = "aeeeiiiioooauuuaeiou"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.

Example 3:

Input: word = "a"
Output: 0
Explanation: There is no beautiful substring, so return 0.

Constraints:

`1 <= word.length <= 5 * 105`

`word` consists of characters `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

【中文翻译】

如果一个字符串满足以下条件，则认为是美丽的：
1. 5个英文元音字母（'a', 'e', 'i', 'o', 'u'）每一个都必须至少出现一次。
2. 字母必须按字母顺序排列（即所有 'a' 在 'e' 之前，所有 'e' 在 'i' 之前，等等）。

例如，字符串 "aeiou" 和 "aaaaaaeiiiioou" 是美丽的，但 "uaeio"、"aeoiu" 和 "aaaeeeooo" 不是。

给定一个由英文元音字母组成的字符串 `word`，返回 `word` 中最长美丽子串的长度。如果不存在这样的子串，返回0。

示例：
输入：word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
输出：13
解释：最长美丽子串是 "aaaaeiiiiouuu"，长度为13。

"""

from typing import List, Optional


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_len = 0
        left = 0
        unique_count = 1  # 当前窗口中不同元音的数量

        for right in range(1, len(word)):
            if word[right] < word[right - 1]:
                # 顺序被破坏，重置窗口
                left = right
                unique_count = 1
            elif word[right] > word[right - 1]:
                unique_count += 1

            if unique_count == 5:
                max_len = max(max_len, right - left + 1)

        return max_len










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 状态机 / 滑动窗口。遍历字符串，维护当前窗口中不同元音的数量。
# 当前字符 >= 前一个字符时，顺序正确；如果当前字符 > 前一个字符，
# 说明遇到新元音，unique_count++；如果当前字符 < 前一个字符，
# 顺序被破坏，重置窗口起点和计数。当unique_count == 5时更新最大长度。
#
# 时间复杂度: O(N)，一次遍历
# 空间复杂度: O(1)，只使用常数变量
#
# 关键点:
# - 元音字母的自然顺序：a < e < i < o < u
# - 顺序被破坏时重置窗口到当前位置
# - 只有unique_count == 5时才可能成为答案
