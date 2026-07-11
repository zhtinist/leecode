"""
LeetCode #2414 - Length of the Longest Alphabetical Continuous Substring
最长的字母序连续子字符串的长度
https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/

字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 `"abcdefghijklmnopqrstuvwxyz"` 的任意子字符串都是 字母序连续字符串 。
例如，`"abc"` 是一个字母序连续字符串，而 `"acb"` 和 `"za"` 不是。
给你一个仅由小写英文字母组成的字符串 `s` ，返回其 最长 的 字母序连续子字符串 的长度。

示例 1：
输入：s = "abacaba" 输出：2 解释：共有 4 个不同的字母序连续子字符串 "a"、"b"、"c" 和 "ab" 。 "ab" 是最长的字母序连续子字符串。
示例 2：
输入：s = "abcde" 输出：5 解释："abcde" 是最长的字母序连续子字符串。

提示：
`1 <= s.length <= 10^5`
`s` 由小写英文字母组成
"""

from typing import List, Optional


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_len = 1
        cur_len = 1
        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i - 1]) + 1:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1
        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String
#
# 解题思路:
# 一次遍历扫描：维护当前连续子串长度cur_len和全局最大长度max_len。
# 对于每个位置i，若当前字符恰好是前一个字符的字母表后继（ord差1），
# 则cur_len加1；否则重置cur_len为1。每次更新max_len。
#
# 时间复杂度: O(n)，一次遍历字符串。
# 空间复杂度: O(1)，只使用常数额外空间。
#
# 关键点:
# - 字母序连续的定义：相邻字符ASCII码差1。
# - 简单的线性扫描即可解决，无需复杂数据结构。
