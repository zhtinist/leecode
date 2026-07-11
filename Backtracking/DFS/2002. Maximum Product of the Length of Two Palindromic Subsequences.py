"""
LeetCode #2002 - Maximum Product of the Length of Two Palindromic Subsequences
两个回文子序列长度的最大乘积
https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

给你一个字符串 `s` ，请你找到 `s` 中两个 不相交回文子序列 ，使得它们长度的 乘积最大 。两个子序列在原字符串中如果没有任何相同下标的字符，则它们是 不相交 的。
请你返回两个回文子序列长度可以达到的 最大乘积 。
子序列 指的是从原字符串中删除若干个字符（可以一个也不删除）后，剩余字符不改变顺序而得到的结果。如果一个字符串从前往后读和从后往前读一模一样，那么这个字符串是一个 回文字符串 。

示例 1：

输入：s = "leetcodecom" 输出：9 解释：最优方案是选择 "ete" 作为第一个子序列，"cdc" 作为第二个子序列。 它们的乘积为 3 * 3 = 9 。
示例 2：
输入：s = "bb" 输出：1 解释：最优方案为选择 "b" （第一个字符）作为第一个子序列，"b" （第二个字符）作为第二个子序列。 它们的乘积为 1 * 1 = 1 。
示例 3：
输入：s = "accbcaxxcxx" 输出：25 解释：最优方案为选择 "accca" 作为第一个子序列，"xxcxx" 作为第二个子序列。 它们的乘积为 5 * 5 = 25 。

提示：
`2 <= s.length <= 12`
`s` 只含有小写英文字母。
"""

from typing import List, Optional


class Solution:
    def maxProduct(self, s: str) -> int:
        """
        n <= 12, so we can enumerate all subsequences via bitmask.
        For each mask, check if it forms a palindrome.
        Then try all pairs of non-overlapping palindromic masks.
        """
        n = len(s)
        size = 1 << n
        # pal_len[mask] = length of palindromic subsequence for mask
        pal_len = {}

        for mask in range(1, size):
            # Build the subsequence string for this mask
            sub = []
            for i in range(n):
                if mask & (1 << i):
                    sub.append(s[i])
            # Check palindrome
            if sub == sub[::-1]:
                pal_len[mask] = len(sub)

        ans = 0
        masks = list(pal_len.keys())
        m = len(masks)

        for i in range(m):
            for j in range(i + 1, m):
                if masks[i] & masks[j] == 0:  # disjoint
                    ans = max(ans, pal_len[masks[i]] * pal_len[masks[j]])

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, String, Dynamic Programming, Backtracking, Bitmask
#
# 解题思路:
# n <= 12，可以用 bitmask 枚举所有子序列（2^12 = 4096 种）。
# 对于每种 mask，提取对应子序列检查是否是回文，记录其长度。
# 然后枚举所有不相交（mask1 & mask2 == 0）的回文子序列对，
# 计算长度乘积的最大值。
#
# 时间复杂度: O(2^N * N + P^2)，N <= 12, P 为回文子序列数 <= 2^N
# 空间复杂度: O(2^N)，存储回文子序列信息
#
# 关键点:
# - 小规模 N 可以用 bitmask 枚举
# - 判断两个 mask 是否不相交: mask1 & mask2 == 0
# - 字符串回文判断: sub == sub[::-1]
