"""
LeetCode #583 - Delete Operation for Two Strings
中文题名：两个字符串的删除操作
https://leetcode.com/problems/delete-operation-for-two-strings/

Given two words word1 and word2, find the minimum number of steps required to
make word1 and word2 the same, where in each step you can delete one character
in either string.

Example 1:

Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:

The length of given words won't exceed 500.

Characters in given words can only be lower-case letters.

【中文翻译】
给定两个单词 word1 和 word2，找出使 word1 和 word2 相同所需的最少步数。
每一步可以删除两个字符串中任意一个中的一个字符。

示例 1：
    输入："sea", "eat"
    输出：2
    解释：需要一步将 "sea" 变为 "ea"，另一步将 "eat" 变为 "ea"。

注意：
    给定单词的长度不超过 500。
    给定单词中的字符只能是小写字母。
"""

from typing import List, Optional


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Minimum deletions = len(word1) + len(word2) - 2 * LCS(word1, word2).
        LCS is computed via 2D DP with a 1D array optimization.
        """
        m, n = len(word1), len(word2)

        # dp[j] = LCS length for word1[:i] and word2[:j]
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev_diag = 0  # dp[i-1][j-1]
            for j in range(1, n + 1):
                temp = dp[j]  # save dp[i-1][j] before overwriting
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev_diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = temp

        lcs = dp[n]
        return m + n - 2 * lcs



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 问题等价于找出两个字符串的最长公共子序列（LCS）。因为要保持的字符就是 LCS 中的字符，
# 其余字符都需要删除。最终答案为 len(word1) + len(word2) - 2 * LCS。使用一维 DP
# 数组计算 LCS：dp[j] 表示 word1[:i] 和 word2[:j] 的 LCS 长度，通过滚动数组
# 优化空间。
#
# 时间复杂度: O(M * N) — 双重循环遍历两个字符串
# 空间复杂度: O(N) — 一维 DP 数组
#
# 关键点:
# - 核心转换：最少删除步数 = 总长度 - 2 * LCS
# - LCS 标准 DP：字符匹配时 dp[i][j] = dp[i-1][j-1] + 1；否则取 max(dp[i-1][j], dp[i][j-1])
# - 可用一维数组优化空间，需用 prev_diag 保存左上角的值
