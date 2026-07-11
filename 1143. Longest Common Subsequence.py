"""
LeetCode #1143 - Longest Common Subsequence
中文题名：最长公共子序列
https://leetcode.com/problems/longest-common-subsequence/

Given two strings `text1` and `text2`, return the length of their
longest common subsequence.

A subsequence of a string is a new string generated from the original string with
some characters(can be none) deleted without changing the relative order of the remaining
characters. (eg, "ace" is a subsequence of "abcde" while "aec"
is not). A common subsequence of two strings is a subsequence that is
common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

`1 <= text1.length <= 1000`

`1 <= text2.length <= 1000`

The input strings consist of lowercase English characters only.

【中文翻译】
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是。两个字符串的公共子序列是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

示例 1：

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。

示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。

示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。

约束条件：

`1 <= text1.length <= 1000`

`1 <= text2.length <= 1000`

输入的字符串只包含小写英文字符。
"""

from typing import List, Optional


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # dp[i][j] = LCS length of text1[0:i] and text2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 经典二维动态规划问题。定义 dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的最长公共子序列长度：
# 1. 状态定义：dp[i][j] 为 text1 前 i 个字符与 text2 前 j 个字符的 LCS 长度。
# 2. 初始状态：dp[0][*] = 0, dp[*][0] = 0（任一字符串为空时，LCS 长度为 0）。
# 3. 状态转移：
#    - 如果 text1[i-1] == text2[j-1]：dp[i][j] = dp[i-1][j-1] + 1
#      （当前字符相等，可以在之前的 LCS 基础上加 1）
#    - 否则：dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#      （跳过 text1 的当前字符，或跳过 text2 的当前字符，取较大值）
# 4. 最终答案：dp[m][n]。
#
# 时间复杂度: O(m * n) - 需要填充整个 m×n 的 DP 表格
# 空间复杂度: O(m * n) - 需要 m×n 的 DP 表格（可优化至 O(min(m, n))）
#
# 关键点:
# - dp 数组多开一行一列作为空字符串的边界条件
# - 字符相同时由左上角转移，不同时取上方或左方的最大值
# - 空间优化：只需两行滚动数组即可，优化至 O(min(m, n))
# - 这是二维 DP 的入门经典题，体现了"最优子结构"的特性
