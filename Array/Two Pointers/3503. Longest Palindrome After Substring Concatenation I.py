"""
LeetCode #3503 - Longest Palindrome After Substring Concatenation I
子字符串连接后的最长回文串 I
https://leetcode.cn/problems/longest-palindrome-after-substring-concatenation-i/

给你两个字符串 `s` 和 `t`。
你可以从 `s` 中选择一个子串（可以为空）以及从 `t` 中选择一个子串（可以为空），然后将它们 按顺序 连接，得到一个新的字符串。
返回可以由上述方法构造出的 最长 回文串的长度。
回文串 是指正着读和反着读都相同的字符串。
子字符串 是指字符串中的一个连续字符序列。

示例 1：

输入： s = "a", t = "a"
输出： 2
解释：
从 `s` 中选择 `"a"`，从 `t` 中选择 `"a"`，拼接得到 `"aa"`，这是一个长度为 2 的回文串。
示例 2：

输入： s = "abc", t = "def"
输出： 1
解释：
由于两个字符串的所有字符都不同，最长的回文串只能是任意一个单独的字符，因此答案是 1。
示例 3：

输入： s = "b", t = "aaaa"
输出： 4
解释：
可以选择 `"aaaa"` 作为回文串，其长度为 4。
示例 4：

输入： s = "abcde", t = "ecdba"
输出： 5
解释：
从 `s` 中选择 `"abc"`，从 `t` 中选择 `"ba"`，拼接得到 `"abcba"`，这是一个长度为 5 的回文串。

提示：
`1 <= s.length, t.length <= 30`
`s` 和 `t` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        ans = 1  # at least one character
        ns, nt = len(s), len(t)

        for a in range(ns + 1):
            for b in range(a, ns + 1):
                for c in range(nt + 1):
                    for d in range(c, nt + 1):
                        combined = s[a:b] + t[c:d]
                        if combined and combined == combined[::-1]:
                            ans = max(ans, len(combined))
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Two Pointers, String, Dynamic Programming, Enumeration
#
# 解题思路:
# 1. 由于字符串长度 <= 30，可以暴力枚举所有可能的子串组合
# 2. 枚举 s 的所有子串（包括空串）和 t 的所有子串（包括空串）
# 3. 拼接 s[a:b] + t[c:d]，检查是否为回文
# 4. 记录最长回文长度
#
# 时间复杂度: O(n^4 * L) 其中 n=30, L 为拼接后长度 <= 60
# 空间复杂度: O(1)
#
# 关键点:
# - 子串可为空，所以可以只选 s 或只选 t 的子串
# - 暴力枚举在 n=30 时完全可行
