"""
LeetCode #1759 - Count Number of Homogenous Substrings
中文题名：统计同构子字符串的数目
https://leetcode.com/problems/count-number-of-homogenous-substrings/

Given a string `s`, return the number of homogenous substrings of `s`. Since the answer may be too large, return it modulo `109 + 7`.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".

Example 3:

Input: s = "zzzzz"
Output: 15

Constraints:

`1 <= s.length <= 105`

`s` consists of lowercase letters.

【中文翻译】
给定一个字符串 s，返回同构子字符串的数量。同构子字符串是指所有字符都相同的子字符串。
由于答案可能很大，结果对 10^9+7 取模。

示例 1：
输入: s = "abbcccaa"
输出: 13
解释: 同构子字符串："a"出现3次，"aa"出现1次，"b"出现2次，"c"出现3次，"cc"出现1次，"ccc"出现1次。共3+1+2+3+1+1=11...
实际上: "a"*3, "aa"*1, "b"*2, "bb"*1, "c"*3, "cc"*2, "ccc"*1, "a"(最后)*2, "aa"*1 = 3+2+3+2+3 = 13
"""

from typing import List, Optional


class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        length = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                length += 1
            else:
                ans = (ans + length * (length + 1) // 2) % MOD
                length = 1

        ans = (ans + length * (length + 1) // 2) % MOD
        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 统计连续相同字符的长度。对于长度为 L 的连续相同字符段，
# 其包含的同构子字符串数量 = L*(L+1)/2（所有连续子串都是同构的）。
# 遍历字符串，统计每个相同字符段的长度，累加公式结果。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 一段长度为 L 的同字符段产生 L*(L+1)/2 个同构子串
# - 只需一次遍历，不断更新当前连续段长度
# - 中途遇到不同字符时结算当前段
