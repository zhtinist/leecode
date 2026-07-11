"""
LeetCode #2767 - Partition String Into Minimum Beautiful Substrings
将字符串分割为最少的美丽子字符串
https://leetcode.cn/problems/partition-string-into-minimum-beautiful-substrings/

给你一个二进制字符串 `s` ，你需要将字符串分割成一个或者多个 子字符串  ，使每个子字符串都是 美丽 的。
如果一个字符串满足以下条件，我们称它是 美丽 的：
它不包含前导 0 。
它是 `5` 的幂的 二进制 表示。
请你返回分割后的子字符串的 最少 数目。如果无法将字符串 `s` 分割成美丽子字符串，请你返回 `-1` 。
子字符串是一个字符串中一段连续的字符序列。

示例 1：
输入：s = "1011" 输出：2 解释：我们可以将输入字符串分成 ["101", "1"] 。 - 字符串 "101" 不包含前导 0 ，且它是整数 5^1 = 5 的二进制表示。 - 字符串 "1" 不包含前导 0 ，且它是整数 5^0 = 1 的二进制表示。 最少可以将 s 分成 2 个美丽子字符串。
示例 2：
输入：s = "111" 输出：3 解释：我们可以将输入字符串分成 ["1", "1", "1"] 。 - 字符串 "1" 不包含前导 0 ，且它是整数 5^0 = 1 的二进制表示。 最少可以将 s 分成 3 个美丽子字符串。
示例 3：
输入：s = "0" 输出：-1 解释：无法将给定字符串分成任何美丽子字符串。

提示：
`1 <= s.length <= 15`
`s[i]` 要么是 `'0'` 要么是 `'1'` 。
"""

from typing import List, Optional


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        n = len(s)
        powers_of_5 = set()
        val = 1
        for _ in range(10):
            powers_of_5.add(bin(val)[2:])
            val *= 5

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if sub[0] != '0' and sub in powers_of_5:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Dynamic Programming, Backtracking
#
# 解题思路:
# 由于 s 长度最多 15，可以暴力 DP。预计算 5 的幂的二进制表示字符串（5^0 到 5^9 足够覆盖）。
# dp[i] 表示前 i 个字符的最少分割数。枚举 j < i，若子串 s[j:i] 是美丽子串（无前导 0 且是 5 的幂的二进制），则 dp[i] = min(dp[i], dp[j] + 1)。
#
# 时间复杂度: O(n^2) 其中 n <= 15
# 空间复杂度: O(n)
#
# 关键点:
# - n <= 15 允许 O(n^2) 的 DP 暴力枚举
# - 5 的幂增长很快，5^9 = 1953125 的二进制长度只有 21 位，足够覆盖
# - 美丽子串不能有前导 0，所以必须检查 sub[0] != '0'
