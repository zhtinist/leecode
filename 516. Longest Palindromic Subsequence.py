"""
LeetCode #516 - Longest Palindromic Subsequence
中文题名：最长回文子序列
https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s. You may assume
that the maximum length of s is 1000.

Example 1:

Input:

"bbbab"

Output:

4

One possible longest palindromic subsequence is "bbbb".

Example 2:

Input:

"cbbd"

Output:

2

One possible longest palindromic subsequence is "bb".

【中文翻译】
给定一个字符串 s，找到其中最长的回文子序列的长度。可以假设 s 的最大长度为 1000。

示例 1：
    输入："bbbab"
    输出：4
    一个可能的最长回文子序列是 "bbbb"。

示例 2：
    输入："cbbd"
    输出：2
    一个可能的最长回文子序列是 "bb"。
"""

from typing import List, Optional


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j] = s[i..j] 中最长回文子序列的长度
        dp = [[0] * n for _ in range(n)]

        # 从右下角向左上角遍历，保证子问题已解决
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划：定义 dp[i][j] 表示子串 s[i..j] 中的最长回文子序列长度。
# 基本情况：dp[i][i] = 1（单个字符本身是回文）。
# 状态转移：若 s[i] == s[j]，则这两个字符可以分别加在内部回文子序列的两端，
#   dp[i][j] = dp[i+1][j-1] + 2；
# 否则，去掉一端取最大值：dp[i][j] = max(dp[i+1][j], dp[i][j-1])。
# 遍历顺序：i 从右向左，j 从左向右，确保计算 dp[i][j] 时 dp[i+1][j-1] 等子问题已求解。
#
# 时间复杂度: O(N^2) — 两层循环遍历所有子区间
# 空间复杂度: O(N^2) — 二维 dp 数组；可优化至 O(N) 但实现较复杂
#
# 关键点:
# - 遍历顺序：i 从 n-1 到 0，j 从 i+1 到 n-1，保证依赖的子问题先计算
# - 与 #5 最长回文子串的区别：子串必须连续，子序列可以不连续
# - 与 #1312 让字符串成为回文串的最少插入次数等价（总长 - LPS 长度）
