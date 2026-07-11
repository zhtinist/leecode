"""
LeetCode #712 - Minimum ASCII Delete Sum for Two Strings
中文题名：两个字符串的最小ASCII删除和
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Given two strings `s1, s2`, find the lowest ASCII sum of deleted characters to
make two strings equal.

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

Note:

`0 < s1.length, s2.length <= 1000`.

All elements of each string will have an ASCII value in `[97, 122]`.

【中文翻译】
给定两个字符串 `s1, s2`，找到使两个字符串相等所需删除字符的最小 ASCII 和。

示例 1：

输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 从 "sea" 中删除 "s" 将 115 加到总和。
从 "eat" 中删除 "t" 将 116 加到总和。
最终，两个字符串相等，115 + 116 = 231 是实现这一目标的最小总和。

示例 2：

输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 从 "delete" 中删除 "dee" 将其变为 "let"，将 100[d] + 101[e] + 101[e] 加到总和。
从 "leet" 中删除 "e" 将 101[e] 加到总和。
最终，两个字符串都等于 "let"，答案为 100 + 101 + 101 + 101 = 403。
如果我们将两个字符串都变成 "lee" 或 "eet"，会得到 433 或 417，这些值更大。

注意：

`0 < s1.length, s2.length <= 1000`。

每个字符串的所有字符的 ASCII 值在 `[97, 122]` 范围内。
"""

from typing import List, Optional


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1])
                    )
        return dp[m][n]









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划，类似于求 LCS（最长公共子序列）的变体。
# 定义 dp[i][j] = s1 的前 i 个字符和 s2 的前 j 个字符，使它们相等所需删除的最小 ASCII 和。
# 初始化：
# - dp[i][0] = 删除 s1 前 i 个字符的 ASCII 和
# - dp[0][j] = 删除 s2 前 j 个字符的 ASCII 和
# 转移方程：
# - 如果 s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]（保留这两个字符）
# - 否则: dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
#   即删除 s1 的当前字符或删除 s2 的当前字符，取较小值。
#
# 时间复杂度: O(m*n)
# 空间复杂度: O(m*n) - 可优化到 O(n) 使用一维数组
#
# 关键点:
# - 本质是带权重的 LCS 变体（权重为 ASCII 码）
# - dp[i][j] 含义是使前 i 和前 j 个字符相等的最小删除 ASCII 和
# - 初始化第一行和第一列
