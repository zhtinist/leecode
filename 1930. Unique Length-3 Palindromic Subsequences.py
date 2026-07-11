"""
LeetCode #1930 - Unique Length-3 Palindromic Subsequences
长度为 3 的不同回文子序列
https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/

给你一个字符串 `s` ，返回 `s` 中 长度为 3 的不同回文子序列 的个数。
即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。
回文 是正着读和反着读一样的字符串。
子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。
例如，`"ace"` 是 `"abcde"` 的一个子序列。

示例 1：
输入：s = "aabca" 输出：3 解释：长度为 3 的 3 个回文子序列分别是： - "aba" ("aabca" 的子序列) - "aaa" ("aabca" 的子序列) - "aca" ("aabca" 的子序列)
示例 2：
输入：s = "adc" 输出：0 解释："adc" 不存在长度为 3 的回文子序列。
示例 3：
输入：s = "bbcbaba" 输出：4 解释：长度为 3 的 4 个回文子序列分别是： - "bbb" ("bbcbaba" 的子序列) - "bcb" ("bbcbaba" 的子序列) - "bab" ("bbcbaba" 的子序列) - "aba" ("bbcbaba" 的子序列)

提示：
`3 <= s.length <= 10^5`
`s` 仅由小写英文字母组成
"""

from typing import List, Optional


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        # For each character (a-z), find its first and last occurrence
        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        result = 0
        for ch in first:
            l, r = first[ch], last[ch]
            if r - l >= 2:
                # Count unique characters between first and last occurrence
                # The palindrome is ch + middle_char + ch
                middle_chars = set()
                for i in range(l + 1, r):
                    middle_chars.add(s[i])
                result += len(middle_chars)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Hash Table, String, Prefix Sum
#
# 解题思路:
# 长度为3的回文子序列形式为 "aba"（两端字符相同）。
# 1. 对于每个字符 ch（作为两端字符），找到其在字符串中的
#    第一次和最后一次出现位置。
# 2. 如果这两个位置之间有至少一个字符，则该区间内所有不同字符
#    都可以作为中间字符，形成回文子序列 "ch + mid + ch"。
# 3. 对于每个 ch，统计其首尾位置之间不同字符的数量。
# 4. 累加得到总数（自动去重因为每个 ch 和中间字符的组合是唯一的）。
#
# 时间复杂度: O(n * 26) = O(n) — 遍历 26 个字符，每个字符扫描区间
# 空间复杂度: O(26) = O(1) — first/last 最多 26 个键
#
# 关键点:
# - 回文子序列形式固定为两端相同
# - 首次和末次出现位置之间的所有字符都可以作为中间字符
# - 不同 (ch, mid) 组合对应不同的回文子序列
# - 使用 set 对中间字符去重
