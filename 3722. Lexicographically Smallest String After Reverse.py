"""
LeetCode #3722 - Lexicographically Smallest String After Reverse
反转后字典序最小的字符串
https://leetcode.cn/problems/lexicographically-smallest-string-after-reverse/

给你一个由小写英文字母组成的、长度为 `n` 的字符串 `s`。
你 必须执行 恰好 一次操作：选择一个整数 `k`，满足 `1 <= k <= n`，然后执行以下两个选项之一：
反转 `s` 的 前 `k` 个字符，或
反转 `s` 的 后 `k` 个字符。
返回在 恰好 执行一次此类操作后可以获得的 字典序最小 的字符串。
如果字符串 `a` 和字符串 `b` 在第一个不同的位置上，`a` 中的字母在字母表中比 `b` 中对应的字母出现得更早，则称字符串 `a` 字典序小于 字符串 `b`。如果前 `min(a.length, b.length)` 个字符都相同，则较短的字符串字典序较小。

示例 1:

输入: s = "dcab"
输出: "acdb"
解释:
选择 `k = 3`，反转前 3 个字符。
将 `"dca"` 反转为 `"acd"`，得到的字符串 `s = "acdb"`，这是可获得的字典序最小的字符串。
示例 2:

输入: s = "abba"
输出: "aabb"
解释:
选择 `k = 3`，反转后 3 个字符。
将 `"bba"` 反转为 `"abb"`，得到的字符串是 `"aabb"`，这是可获得的字典序最小的字符串。
示例 3:

输入: s = "zxy"
输出: "xzy"
解释:
选择 `k = 2`，反转前 2 个字符。
将 `"zx"` 反转为 `"xz"`，得到的字符串是 `"xzy"`，这是可获得的字典序最小的字符串。

提示:
`1 <= n == s.length <= 1000`
`s` 由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def lexicographicallySmallestAfterReverse(self, s: str) -> str:
        n = len(s)
        ans = s
        for k in range(1, n + 1):
            # Reverse first k characters
            cand1 = s[:k][::-1] + s[k:]
            if cand1 < ans:
                ans = cand1
            # Reverse last k characters
            cand2 = s[:n - k] + s[n - k:][::-1]
            if cand2 < ans:
                ans = cand2
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Two Pointers, Binary Search, Enumeration
#
# 解题思路:
# 枚举所有可能的 k（1 到 n），对于每个 k：
# 1. 反转前 k 个字符：s[:k][::-1] + s[k:]
# 2. 反转后 k 个字符：s[:n-k] + s[n-k:][::-1]
# 取所有候选字符串中字典序最小的。由于 n <= 1000，O(n^2) 的暴力枚举可以通过。
#
# 时间复杂度: O(n^2)
# 空间复杂度: O(n)
#
# 关键点:
# - 注意是恰好执行一次操作，不能不做
# - 全面枚举两种反转方式的所有可能 k
