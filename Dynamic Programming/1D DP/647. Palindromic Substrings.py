"""
LeetCode #647 - Palindromic Substrings
中文题名：回文子串
https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different
substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

The input string length won't exceed 1000.

【中文翻译】
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为不同的子串。

示例 1：

输入："abc"
输出：3
解释：三个回文子串："a", "b", "c"。

示例 2：

输入："aaa"
输出：6
解释：六个回文子串："a", "a", "a", "aa", "aa", "aaa"。

注意：

输入的字符串长度不会超过 1000。
"""

from typing import List, Optional


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用中心扩展法。对于长度为 n 的字符串，共有 2n-1 个可能的回文中心：
# - n 个单字符中心（奇数长度回文）
# - n-1 个双字符之间的中心（偶数长度回文）
# 对于每个中心，向两边扩展，只要左右字符相等就计数加一。
# 巧妙地将奇数和偶数回文统一处理：center//2 为左指针起始位置，
# center%2 用于调整右指针（奇数回文时左右相同，偶数回文时右=左+1）。
#
# 时间复杂度: O(n^2) - 每个中心最多扩展 n 次
# 空间复杂度: O(1) - 仅使用常数额外空间
#
# 关键点:
# - 中心扩展法统一处理奇偶回文
# - 共有 2n-1 个回文中心
# - 动态规划也可解（O(n^2) 时间和空间），中心扩展法空间更优
# - 马拉车算法 (Manacher) 可做到 O(n) 时间，但对于本题 n<=1000 中心扩展已足够
