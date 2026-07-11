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
# ── KMP 算法是什么 ────────────────────────────────────────────────────────────
#
# KMP（Knuth-Morris-Pratt）是 **单模式串匹配** 算法：在文本串 text 里找模式串
# pattern 第一次出现的位置。
#
# 暴力做法：pattern 每个对齐位置都从第一个字符重新比，最坏 O(n×m)。
#
# KMP 的核心思想：**失配时不要从头比**，利用「已经匹配上的前缀」信息，把
# pattern 向右滑动到下一个可能成功的位置，文本指针 i 不回退。
#
# 依赖预处理数组 LPS（也叫 next / fail）：
#   lps[k] = pattern[0..k] 这段的「最长相同真前缀与真后缀」的长度。
#
#   pattern = "ababc"
#     k:     0 1 2 3 4
#     char:  a b a b c
#     lps:   0 0 1 2 0
#
#   lps[3]=2：子串 "abab" 前后缀最长公共为 "ab"，长度 2。
#   含义：若在更长的匹配中，下一位失配，至少前 2 个字符已对齐，可从位置 2 继续比。
#
# 匹配时（text 下标 i，pattern 下标 j）：
#   字符相等 → i++, j++
#   字符不等 → j = lps[j-1]（pattern 回退，i 不动）
#   j 归零仍不等 → i++（彻底对不上，文本前进一位）
#
# 为什么 O(n+m)：i 只增不减；j 每次回退都变小，总回退次数有上界。
#
# KMP 的两类用法：
#   1. 标准匹配：在 text 里搜 pattern。
#   2. 只算 LPS：不搜模式，用 LPS 求「最长 border / 最长公共前后缀」——本题即此类。
#
# ── 题意 ──────────────────────────────────────────────────────────────────────
#
# 只能在字符串 **前面** 加字符，让结果变成回文，且加得越少越好。
#
# 例：s = "abcd"
#   - 最长回文前缀是 "a"（只有首字符）
#   - 后缀 "bcd" 不是回文 → 需要把 "bcd" 的翻转 "dcb" 补到前面
#   - 答案："dcb" + "abcd" = "dcbabcd"
#
# 核心转化：找 s 的 **最长回文前缀**，长度记为 L。
#   只需把 s[L:] 翻转后接到前面，就是最短方案。
#
# ── KMP 与本题的关系 ──────────────────────────────────────────────────────────
#
# KMP 的 LPS（Longest Prefix Suffix）数组：
#   lps[i] = 子串 text[0..i] 的「最长相同真前缀与真后缀」的长度。
#
#   例：text = "ababa"
#         i:  0 1 2 3 4
#         lps:0 0 1 2 3
#   lps[4]=3 表示 "ababa" 前后缀最长公共长度 3，即 "aba"。
#
# 回文前缀 ⟺ 正着读的前缀 = 反着读的后缀
#
#   s 的回文前缀 "aacecaa"  ⟺  s 的前缀  ==  reverse(s) 的后缀
#
# 所以构造：combined = s + '#' + reverse(s)
#
#   '#' 是分隔符，防止匹配「跨过」连接点（否则 s 尾部可能错误对上 rev 头部）。
#
#   combined 的 lps 最后一位 = s 与 reverse(s) 的最长公共前后缀长度
#                            = s 的最长回文前缀长度 L
#
# ── 示例走读：s = "aacecaaa" ──────────────────────────────────────────────────
#
#   rev = "aaacecaa"
#   combined = "aacecaaa#aaacecaa"
#
#   lps[-1] = 7 → 最长回文前缀 "aacecaa"（长度 7）
#   需补前缀 = rev[:len(s)-7] = rev[:1] = "a"
#   答案 = "a" + "aacecaaa" = "aaacecaaa"
#
# ── LPS 计算过程（KMP 核心循环）──────────────────────────────────────────────
#
#   j = 当前已匹配的前缀长度（也是下一个要比较的位置）
#   扫 combined，i 从 1 到 n-1：
#
#     若 combined[i] != combined[j]：
#         j = lps[j-1]   # 前缀缩短，回退（利用已算好的 lps，避免重头比）
#     若 combined[i] == combined[j]：
#         j += 1; lps[i] = j
#
#   不匹配时回退到 lps[j-1]，是 KMP 能在 O(n) 完成匹配的关键。
#
# ── 最终公式 ──────────────────────────────────────────────────────────────────
#
#   return rev[:len(s) - lps[-1]] + s
#
#   rev[:len(s)-L] = 非回文后缀的翻转，补到前面即可。
#
# 时间复杂度: O(n)   空间复杂度: O(n)

