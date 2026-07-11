"""
LeetCode #3138 - Minimum Length of Anagram Concatenation
同位字符串连接的最小长度
https://leetcode.cn/problems/minimum-length-of-anagram-concatenation/

给你一个字符串 `s` ，它由某个字符串 `t` 和若干 `t`  的 同位字符串 连接而成。
请你返回字符串 `t` 的 最小 可能长度。
同位字符串 指的是重新排列一个字符串的字母得到的另外一个字符串。例如，"aab"，"aba" 和 "baa" 是 "aab" 的同位字符串。

示例 1：

输入：s = "abba"
输出：2
解释：
一个可能的字符串 `t` 为 `"ba"` 。
示例 2：

输入：s = "cdef"
输出：4
解释：
一个可能的字符串 `t` 为 `"cdef"` ，注意 `t` 可能等于 `s` 。
示例 3：
输入：s = "abcbcacabbaccba"
输出：3

提示：
`1 <= s.length <= 10^5`
`s` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        # 检查每个可能的t长度L（L必须整除n）
        for L in range(1, n + 1):
            if n % L != 0:
                continue
            blocks = n // L
            # 第一个块的字符计数作为参照
            ref = [0] * 26
            for ch in s[:L]:
                ref[ord(ch) - 97] += 1

            ok = True
            for b in range(1, blocks):
                cnt = [0] * 26
                start = b * L
                for j in range(start, start + L):
                    cnt[ord(s[j]) - 97] += 1
                if cnt != ref:
                    ok = False
                    break
            if ok:
                return L
        return n



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Counting
#
# 解题思路:
# 如果可以分割成长度为L的块，每个块必须是同构的（字符计数相同）。
# 枚举n的所有因子作为候选L，从小到大尝试。对每个候选L，将第一个块的字符计数作为模板，
# 然后检查后续每个块的字符计数是否与模板一致。第一个满足条件的L即为答案。
#
# 时间复杂度: O(n * d(n))，其中d(n)为n的因子个数（n<=10^5时最多约128个）
# 空间复杂度: O(1)（固定26个字母的计数数组）
#
# 关键点:
# - 同位字符串意味着字符计数相同
# - t的长度必须整除s的长度
# - 从小到大枚举L，第一次成功即为最小长度
